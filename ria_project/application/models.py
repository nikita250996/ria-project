from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db.models.signals import post_save
from django.dispatch import receiver


class EmployeeInfo(models.Model):
    """Сотрудник УИС

    Поля:
        ground Код площадки СФУ
        # name Имя
        # surname Фамилия
        jobrole Должность
        home_address Домашний адрес
        birth_date Дата рождения
        #  email Адрес электронной почты
        mobile_phone Номер мобильного телефона
        home_phone Номер домашнего телефона
    """

    ground = models.ForeignKey(to='Ground', on_delete=models.PROTECT, null=True, verbose_name='Код площадки СФУ', help_text='Код площадки СФУ ???. Например, 1')

    # TODO ВТОРИЧНОЙ важности job_title?
    jobrole = models.CharField(max_length=100, null=True, verbose_name='Должность', help_text='Должность сотрудника УИС. Например, ???')
    home_address = models.CharField(max_length=200, null=True, verbose_name='Домашний адрес', help_text='Домашний адрес сотрудника УИС. Например, ???')
    birth_date = models.DateField(null=True, verbose_name='Дата рождения', help_text='Дата рождения сотрудника УИС. Например, ???')
    mobile_phone = models.CharField(max_length=20, null=True, verbose_name='Номер мобильного телефона', help_text='Номер мобильного телефона сотрудника УИС. Например, +78005553535')
    home_phone = models.CharField(max_length=20, null=True, verbose_name='Номер домашнего телефона', help_text='Номер домашнего телефона сотрудника УИС. Например, ???')

    class Meta:
        verbose_name = 'сотрудника УИС'
        verbose_name_plural = 'Сотрудники УИС'

    def __str__(self):
        return str(self.user)

class User(AbstractUser):
    employee_info = models.OneToOneField(EmployeeInfo, on_delete=models.CASCADE, related_name="user", blank=True, null=True, verbose_name='???', help_text='???. Например, ???')
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество', help_text='Отчество сотрудника УИС. Например, Рамильевич')


class CommercializationType(models.Model):
    """Тип коммерциализации РИД

    Поля:
        name Наименование
    """
    name = models.CharField(max_length=100, blank=False, verbose_name='Наименование',
                            help_text='Тип коммерциализации РИД.')

    class Meta:
        verbose_name = 'тип коммерциализации РИД'
        verbose_name_plural = 'Типы коммерциализации РИД'

    def __str__(self):
        return self.name


class ContractType(models.Model):
    """Тип договора на РИД

    Поля:
        name Наименование
    """

    name = models.CharField(max_length=100, blank=False, verbose_name='Наименование',
                            help_text='Тип договора на РИД.')

    class Meta:
        verbose_name = 'тип договора на РИД'
        verbose_name_plural = 'Типы договора на РИД'

    def __str__(self):
        return self.name


class Ground(models.Model):
    """Площадка СФУ

    Поля:
        ground_code Код
        phone Телефонный номер
        index Индекс
        address Физический адрес
    """

    ground_code = models.IntegerField(unique=True, verbose_name='Код', help_text='Код площадки СФУ. Например, 1')
    phone = models.CharField(max_length=50, null=True, verbose_name='Телефонный номер',
                             help_text='Телефонный номер площадки СФУ. Например, +78005553535')
    index = models.CharField(max_length=20, null=True, verbose_name='Индекс',
                             help_text='Индекс площадки СФУ. Например, 660074')
    address = models.CharField(max_length=100, blank=False, null=True, verbose_name='Физический адрес',
                               help_text='Физический адрес площадки СФУ. Например, пр. Свободный 79.')

    class Meta:
        verbose_name = 'площадку СФУ'
        verbose_name_plural = 'Площадки СФУ'

    def __str__(self):
        return 'Площадка СФУ №' + str(self.ground_code)


class IntellectualPropertyType(models.Model):
    """Тип РИД

    Поля:
        name Наименование
        protection_document_name Название охранного документа
        validity Срок действия
        renewal Срок продления
        pay_period Период оплаты
    """

    name = models.CharField(max_length=100, blank=False, null=True, verbose_name='Наименование',
                            help_text='Наименование РИД.')
    protection_document_name = models.CharField(max_length=100, blank=False, null=True,
                                                verbose_name='Охранный документ',
                                                help_text='Охранный документ.')
    validity = models.IntegerField(null=True, verbose_name='Срок действия',
                                   help_text='Срок действия ???. Например, ???')
    renewal = models.IntegerField(null=True, verbose_name='Срок продления',
                                  help_text='Введите срок продления.')
    pay_period = models.IntegerField(null=True, verbose_name='Период оплаты',
                                     help_text='Введите период оплаты.')

    class Meta:
        verbose_name = 'тип РИД'
        verbose_name_plural = 'Типы РИД'

    def __str__(self):
        return self.name


class Person(models.Model):

    def __str__(self):
        if hasattr(self, 'privateperson'):
            return str(self.privateperson)
        return str(self.legalperson)


class Country(models.Model):
    """Страна

    Поля:
        code Код
        name Название
    """

    code = models.CharField(max_length=10, verbose_name='Код', help_text='Код страны. Например, RU')
    name = models.CharField(max_length=100, blank=False, verbose_name='Название',
                            help_text='Название страны. Например, Россия')

    class Meta:
        verbose_name = 'страну'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.code


class Request(models.Model):
    """Заявка на РИД

    Поля:
        number Номер
        protection_title Охранный документ
        ip_name Название
        abridgement Реферат
        ground Площадка СФУ
        ip_type Тип
        ipc Международная классификация
        bulletin_number Номер бюллетеня
        bulletin_date Дата публикации бюллетеня
        priority_date Дата приоритета - дата регистрации РИДа в ОФАП
        send_date Дата отправки запроса
        receipt_date Дата получения охранного документа
        grant_date Дата выдачи ФИПСом охранного документа на РИД
        is_contracted Выполнено ли договору?
        contract_number Номер договора
        contract_date Дата заключения договора
        text Тема
        number_policy_measure Номер программного мероприятия
        note Примечание
        contract_type Вид договора
        provider Исполнитель
        commissioner Руководитель
        owner Патентообладатели
        creator Авторы
        country Страны
    """

    number = models.IntegerField(verbose_name='Номер',
                                 help_text='Номер заявки на РИД.', validators=[MinValueValidator(0)])
    protection_title = models.CharField(max_length=40, blank=False,
                                        verbose_name='Охранный документ', help_text='Номер охранного документа.')
    ip_name = models.CharField(max_length=200, blank=False,
                               verbose_name='Название', help_text='Название РИД.')
    abridgement = models.TextField(verbose_name='Реферат', null=True, blank=True,
                                   help_text='Реферат РИД.')
    ground = models.ForeignKey(to='Ground', on_delete=models.PROTECT,
                               verbose_name='Площадка СФУ', help_text='Номер площадки СФУ.')
    ip_type = models.ForeignKey(to='IntellectualPropertyType', on_delete=models.PROTECT,
                                verbose_name='Тип', help_text='Тип РИД.')
    ipc = models.CharField(max_length=1000, null=True, blank=True, default='',
                           verbose_name='МПК', help_text='Международная патентная классификация.')
    priority_date = models.DateTimeField(verbose_name='Дата приоритета',
                                         help_text='Дата регистрации РИДа в ОФАП.')
    send_date = models.DateTimeField(verbose_name='Дата подачи заявки',
                                     help_text='Дата подачи заявки.')
    grant_date = models.DateTimeField(verbose_name='Дата выдачи патента',
                                      help_text='Дата выдачи ФИПСом охранного документа на РИД.')
    receipt_date = models.DateTimeField(verbose_name='Дата получения охранного документа',
                                        help_text='Дата получения охранного документа отделом УИС.')
    bulletin_number = models.IntegerField(verbose_name='Номер бюллетеня', null=True, blank=True,
                                          validators=[MinValueValidator(1), MaxValueValidator(100)],
                                          help_text='Номер официального бюллетеня «Изобретения. Полезные модели»')
    bulletin_date = models.DateTimeField(verbose_name='Дата публикации бюллетеня', null=True, blank=True,
                                         help_text='Дата публикации официального бюллетеня '
                                                   '«Изобретения. Полезные модели»')
    # Договор
    is_contracted = models.BooleanField(verbose_name='Договор', blank=True, default=False,
                                        help_text='Выполнено ли договору?.')
    contract_number = models.CharField(max_length=50, blank=True,
                                       verbose_name='Номер договора',
                                       help_text='Номер договора.')
    contract_type = models.ForeignKey(to='ContractType', blank=True,
                                      verbose_name='Вид договора', help_text='Вид договора.',
                                      on_delete=models.PROTECT)
    contract_date = models.DateTimeField(verbose_name='Дата заключения договора', blank=True,
                                         help_text='Дата заключения договора.')

    text = models.TextField(verbose_name='Тема', help_text='Тема. ')
    number_policy_measure = models.CharField(max_length=50, verbose_name='Номер программного мероприятия',
                                             help_text='Номер программного мероприятия.')
    note = models.TextField(verbose_name='Примечание',
                            help_text='Дополнительная информация.')
    provider = models.ForeignKey(to='Person', on_delete=models.PROTECT, related_name='provider',
                                 verbose_name='Исполнитель', help_text='Исполнитель.')
    commissioner = models.ForeignKey(to='Person', on_delete=models.PROTECT, related_name='commissioner',
                                     verbose_name='Руководитель', help_text='Руководитель ???. Например, ???')
    owners = models.ManyToManyField(Person, related_name='ip_owner', verbose_name='Патентообладатели',
                                    help_text='Патентообладатели.')
    creators = models.ManyToManyField(Person, verbose_name='Авторы',
                                      help_text='Перечислите авторов.')
    countries = models.ManyToManyField(Country, verbose_name='Страны',
                                     help_text='Название выдавшей патент страны.')

    class Meta:
        verbose_name = 'заявку на РИД'
        verbose_name_plural = 'Заявки на РИД'

    def __str__(self):
        return 'Заявка на РИД №' + str(self.number)


        # Вторичные задачи


class Duty(models.Model):
    """Пошлина

    Поля:
        order_number Номер перечня
        name Наименование
        size Размер
        intellectual_property_type Типы РИД
    """

    # TODO ВТОРИЧНОЙ важности help_text
    order_number = models.CharField(max_length=50, null=True, verbose_name='Номер перечня', help_text='Номер перечня ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    name = models.CharField(max_length=250, null=True, verbose_name='Наименование', help_text='Наименование пошлины. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    size = models.FloatField(null=True, verbose_name='Размер', help_text='Размер пошлины. Например, ???')
    # TODO ВТОРИЧНОЙ важности intellectual_property_types?, help_text
    intellectual_property_type = models.ManyToManyField(IntellectualPropertyType, verbose_name='Типы РИД', help_text='Типы РИД ???. Например, ???')

    class Meta:
        verbose_name = 'пошлину'
        verbose_name_plural = 'Пошлины'

    def __str__(self):
        return self.name


class IntellectualProperty(models.Model):
    """РИД

    Поля:
        request_number Номер заявки
        protection_title Охранный документ
        name Название
        abridgement Реферат
        ground Номер площадки СФУ
        type_fk Тип
        bulletin_number Номер бюллетеня
        bulletin_date Дата публикации бюллетеня
        priority_date Дата приоритета
        grant_date Дата получения охранного документа
        duty_payments Оплаты пошлины
    """

    ipc = models.CharField(max_length=1000, null=True, blank=True, default='',
                           verbose_name='МПК', help_text='Международная патентная классификация.')
    # TODO ВТОРИЧНОЙ важности help_text
    request_number = models.IntegerField(verbose_name='Номер заявки', help_text='Номер заявки ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    protection_title = models.CharField(max_length=40, verbose_name='Охранный документ', help_text='Охранный документ ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    name = models.CharField(max_length=200, blank=False, verbose_name='Название', help_text='Название РИД. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    abridgement = models.TextField(verbose_name='Реферат', help_text='Реферат РИД. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    ground = models.ForeignKey(to='Ground', on_delete=models.PROTECT, verbose_name='Номер площадки СФУ', help_text='Номер площадки СФУ ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    type_fk = models.ForeignKey(to='IntellectualPropertyType', on_delete=models.PROTECT, verbose_name='Тип', help_text='Тип РИД. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    bulletin_number = models.IntegerField(verbose_name='Номер бюллетеня', help_text='Номер бюллетеня ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    bulletin_date = models.DateField(verbose_name='Дата публикации бюллетеня', help_text='Дата публикации бюллетеня ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    priority_date = models.DateField(verbose_name='Дата приоритета', help_text='Дата приоритета ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    grant_date = models.DateField(verbose_name='Дата получения охранного документа', help_text='Дата получения охранного документа. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    duty_payments = models.ManyToManyField(Duty, through='Payment', verbose_name='Оплаты пошлин', help_text='Оплаты пошлин ???. Например, ???')

    class Meta:
        verbose_name = 'РИД'
        verbose_name_plural = 'РИД'

    def __str__(self):
        return self.name


class Payment(models.Model):
    """Оплаты пошлин

    Поля:
        duty Пошлина
        intellectual_property РИД
        purchase_order_number Номер платежного поручения
        payment_date Дата оплаты
        posted_date Дата внесения
        paid_amount Сумма оплаты
        note Примечание
    """

    # TODO ВТОРИЧНОЙ важности help_text
    duty = models.ForeignKey(Duty, on_delete=models.PROTECT, verbose_name='Пошлина', help_text='Пошлина ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    intellectual_property = models.ForeignKey(IntellectualProperty, on_delete=models.PROTECT, verbose_name='РИД', help_text='РИД ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    purchase_order_number = models.IntegerField(verbose_name='Номер платежного поручения', help_text='Номер платежного поручения ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    payment_date = models.DateField(verbose_name='Дата оплаты', help_text='Дата оплаты ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    posted_date = models.DateField(verbose_name='Дата внесения', help_text='Дата внесения ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    paid_amount = models.FloatField(verbose_name='Сумма оплаты', help_text='Сумма оплаты ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    note = models.TextField(verbose_name='Примечание', help_text='Примечание ???. Например, ???')
    check_scan = models.ImageField(verbose_name='Чек', help_text='Скан чека')

    class Meta:
        # TODO ВТОРИЧНОЙ важности
        verbose_name = '???'
        verbose_name_plural = 'Оплаты пошлин'

    def __str__(self):
        # TODO ВТОРИЧНОЙ важности Что возвращать?
        return str(self.purchase_order_number)


class ContractIntellectualProperties(models.Model):
    """РИД, выполненный по гранту

    Поля:
        intellectual_property РИД
        number Номер договора
        date Дата подписания договора
        text Тема
        number_policy_measure Номер программного мероприятия
        note Примечание
        contract_type Вид договора
        provider Исполнитель
        commissioner Руководитель
    """

    # TODO ВТОРИЧНОЙ важности help_text
    intellectual_property = models.ForeignKey(to='IntellectualProperty', on_delete=models.PROTECT, verbose_name='РИД', help_text='РИД ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    number = models.CharField(max_length=50, verbose_name='Номер договора', help_text='Номер договора ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    date = models.DateField(verbose_name='Дата подписания договора', help_text='Дата подписания договора ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    text = models.TextField(verbose_name='Тема', help_text='Тема ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    number_policy_measure = models.CharField(max_length=50, verbose_name='Номер программного мероприятия', help_text='Номер программного мероприятия ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    note = models.TextField(verbose_name='Примечание', help_text='Примечание ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    contract_type = models.ForeignKey(to='ContractType', on_delete=models.PROTECT, verbose_name='Вид договора', help_text='Вид договора ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    provider = models.ForeignKey(to='Person', on_delete=models.PROTECT, related_name='prov', verbose_name='Исполнитель', help_text='Исполнитель ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    commissioner = models.ForeignKey(to='Person', on_delete=models.PROTECT, related_name='comm', verbose_name='Руководитель', help_text='Руководитель ???. Например, ???')

    class Meta:
        verbose_name = 'РИД, выполненный по гранту'
        verbose_name_plural = 'РИД, выполненные по гранту'

    def __str__(self):
        # TODO ВТОРИЧНОЙ важности Что возвращать?
        return str(self.intellectual_property)


class IPCommercialization(models.Model):
    """Коммерциализация РИД

    Поля:
        intellectual_property РИД
        reference_number Номер дела
        send_date Дата отправки на регистрацию
        commercialization_type Наименование вида/типа использования РИД
        licencee Лицензиат - получатель лицензии
        version_number ???
        filing_date Дата регистрации договора
        acceptance_delivery_acr Акт сдачи-приемки
        contract_duration Срок действия договора
        agreement_terms Условия договора
        note Примечание
        licenser Лицензиары
    """

    # TODO ВТОРИЧНОЙ важности help_text
    intellectual_property = models.ForeignKey(to='IntellectualProperty', on_delete=models.PROTECT, verbose_name='РИД', help_text='РИД ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    reference_number = models.IntegerField(verbose_name='Номер дела', help_text='Номер дела ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    send_date = models.DateField(verbose_name='Дата отправки на регистрацию', help_text='Дата отправки на регистрацию ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    commercialization_type = models.ForeignKey(to='CommercializationType', on_delete=models.PROTECT, verbose_name='Наименование вида/типа использования РИД', help_text='Наименование вида/типа использования РИД ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    licencee = models.CharField(max_length=200, verbose_name='Лицензиат - получатель лицензии', help_text='Лицензиат - получатель лицензии ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности verbose_name, help_text (номер использования РИД)
    version_number = models.CharField(max_length=50, verbose_name='???', help_text='???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    filing_date = models.DateField(verbose_name='Дата регистрации договора', help_text='Дата регистрации договора ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    acceptance_delivery_acr = models.BooleanField(verbose_name='Акт сдачи-приемки', help_text='Акт сдачи-приемки ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    contract_duration = models.CharField(max_length=100, verbose_name='Срок действия договора', help_text='Срок действия договора ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    agreement_terms = models.TextField(verbose_name='Условия договора', help_text='Условия договора ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    note = models.TextField(verbose_name='Примечание', help_text='Примечание ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности licencers?, help_text
    licenser = models.ManyToManyField(Person, verbose_name='Лицензиары', help_text='Лицензиары ???. Например, ???')

    class Meta:
        # TODO ВТОРИЧНОЙ важности
        verbose_name = '???'
        verbose_name_plural = 'Коммерциализация РИД'

    def __str__(self):
        # TODO ВТОРИЧНОЙ важности Что возвращать?
        return str(self.intellectual_property)


class IntangibleAssets(models.Model):
    """Реестр НМА

    Поля:
        intellectual_property РИД
        date Дата постановки на НМА
        number Номер акта
        book_value Балансовая стоимость
        retirement_date Дата списания
    """

    # TODO ВТОРИЧНОЙ важности help_text
    intellectual_property = models.ForeignKey(to='IntellectualProperty', on_delete=models.PROTECT, verbose_name='РИД', help_text='РИД ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности verbose_name, help_text
    date = models.DateField(verbose_name='Дата постановки на НМА ???', help_text='Дата постановки на НМА ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    number = models.CharField(max_length=10, verbose_name='Номер акта', help_text='Номер акта ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    book_value = models.FloatField(verbose_name='Балансовая стоимость', help_text='Балансовая стоимость ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    retirement_date = models.DateField(verbose_name='Дата списания', help_text='Дата списания ???. Например, ???')

    class Meta:
        # TODO ВТОРИЧНОЙ важности
        verbose_name = '???'
        verbose_name_plural = 'Реестр НМА'

    def __str__(self):
        # TODO ВТОРИЧНОЙ важности Что возвращать?
        return str(self.intellectual_property)


class CardRegister(models.Model):
    """Картотека

    Поля:
        intellectual_property РИД
        status Статус
        refusal_date Дата отказа поддержки
        note Примечание
    """

    # TODO ВТОРИЧНОЙ важности help_text
    intellectual_property = models.ForeignKey(to='IntellectualProperty', on_delete=models.PROTECT, verbose_name='РИД', help_text='РИД ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    status = models.CharField(max_length=200, verbose_name='Статус', help_text='Статус ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    refusal_date = models.DateField(verbose_name='Дата отказа поддержки', help_text='Дата отказа поддержки ???. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    note = models.TextField(verbose_name='Примечание', help_text='Примечание ???. Например, ???')

    class Meta:
        verbose_name = 'Картотека'
        verbose_name_plural = 'Картотека'

    def __str__(self):
        return str(self.intellectual_property)


class PrivatePerson(Person):
    """Физическое лицо

    Поля:
        name Имя
        surname Фамилия
        patronymic Отчество
        work_place Подразделения СФУ: место работы автора (авторов РИД)
    """

    name = models.CharField(max_length=100, blank=False, verbose_name='Имя', help_text='Имя физического лица. Например, Никита')
    surname = models.CharField(max_length=100, blank=False, verbose_name='Фамилия', help_text='Фамилия физического лица. Например, Нурлыгаянов')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', help_text='Отчество физического лица. Например, Рамильевич')
    # TODO ВТОРИЧНОЙ важности help_text
    work_place = models.CharField(max_length=100, blank=False, verbose_name='Подразделения СФУ: место работы автора (авторов РИД)',
                                  help_text='Подразделения СФУ: место работы автора (авторов РИД) ???. Например, ???')

    class Meta:
        verbose_name = 'физическое лицо'
        verbose_name_plural = 'Физические лица'

    def __str__(self):
        return self.full_name() + ", " + self.work_place

    def full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic


class LegalPerson(Person):
    """Юридическое лицо

    Поля:
        name Наименование
        address Физический адрес
        phone Телефонный номер
        fax Факс
        site Адрес сайта
        email Адрес электронной почты
    """

    # TODO ВТОРИЧНОЙ важности help_text
    name = models.CharField(max_length=200, blank=False, null=True, verbose_name='Наименование', help_text='Наименование юридического лица. Например, ???')
    # TODO ВТОРИЧНОЙ важности help_text
    address = models.CharField(max_length=200, blank=False, null=True, verbose_name='Физический адрес', help_text='Физический адрес юридического лица. Например, ???')
    phone = models.CharField(max_length=100, blank=False, null=True, verbose_name='Телефонный номер', help_text='Телефонный номер юридического лица. Например, +78005553535')
    # TODO ВТОРИЧНОЙ важности help_text
    fax = models.CharField(max_length=100, blank=False, null=True, verbose_name='Факс', help_text='Факс юридического лица. Например, ???')
    site = models.CharField(max_length=100, blank=False, null=True, verbose_name='Адрес сайта', help_text='Адрес сайта юридического лица. Например, nikita.ru')
    email = models.CharField(max_length=100, blank=False, null=True, verbose_name='Адрес электронной почты', help_text='Адрес электронной почты юридического лица. Например, nikita25@mail.ru')

    class Meta:
        verbose_name = 'юридическое лицо'
        verbose_name_plural = 'Юридические лица'

    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    if created:
        profile, new = EmployeeInfo.objects.get_or_create(user=instance)