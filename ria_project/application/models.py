# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


class User(AbstractUser):
    """Пользователь

    Поля:
        patronymic Отчество
    """

    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество',
                                  help_text='Отчество сотрудника УИС. Например, Рамильевич')


class EmployeeInfo(models.Model):
    """Сотрудник УИС

    Поля:
        ground Код площадки СФУ
        jobrole Должность
        home_address Домашний адрес
        birth_date Дата рождения
        mobile_phone Номер мобильного телефона
        home_phone Номер домашнего телефона
        user Имя пользователя
    """

    ground = models.ForeignKey(to='Ground', on_delete=models.PROTECT, null=True, verbose_name='Код площадки СФУ',
                               help_text='Код площадки СФУ, на которой трудится сотрудник УИС')
    jobrole = models.CharField(max_length=100, null=True, verbose_name='Должность',
                               help_text='Должность сотрудника УИС')
    home_address = models.CharField(max_length=200, null=True, verbose_name='Домашний адрес',
                                    help_text='Домашний адрес сотрудника УИС')
    birth_date = models.DateField(null=True, verbose_name='Дата рождения',
                                  help_text='Дата рождения сотрудника УИС')
    mobile_phone = models.CharField(max_length=20, null=True, verbose_name='Номер мобильного телефона',
                                    help_text='Номер мобильного телефона сотрудника УИС. Например, +78005553535')
    home_phone = models.CharField(max_length=20, null=True, verbose_name='Номер домашнего телефона',
                                  help_text='Номер домашнего телефона сотрудника УИС')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name='Имя пользователя',
                                help_text='Имя пользователя, к которому привязан сотрудник УИС')

    class Meta:
        verbose_name = 'сотрудник УИС'
        verbose_name_plural = 'Сотрудники УИС'

    def __str__(self):
        return str(self.user)


class CommercializationType(models.Model):
    """Тип коммерциализации РИД

    Поля:
        name Наименование
    """
    name = models.CharField(max_length=100, blank=False, verbose_name='Наименование',
                            help_text='Наименование типа коммерциализации РИД')

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
                            help_text='Наименование типа договора на РИД')

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

    ground_code = models.IntegerField(unique=True, verbose_name='Код',
                                      help_text='Код площадки СФУ. Например, 1')
    phone = models.CharField(max_length=50, null=True, verbose_name='Телефонный номер',
                             help_text='Телефонный номер площадки СФУ. Например, +78005553535')
    index = models.CharField(max_length=20, null=True, verbose_name='Индекс',
                             help_text='Индекс площадки СФУ. Например, 660074')
    address = models.CharField(max_length=100, blank=False, null=True, verbose_name='Физический адрес',
                               help_text='Физический адрес площадки СФУ. Например, проспект Свободный. дом 79')

    class Meta:
        verbose_name = 'площадка СФУ'
        verbose_name_plural = 'Площадки СФУ'

    def __str__(self):
        return 'Площадка №' + str(self.ground_code)


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
                            help_text='Наименование типа РИД')
    protection_document_name = models.CharField(max_length=100, blank=False, null=True,
                                                verbose_name='Название охранного документа',
                                                help_text='Название охранного документа типа РИД')
    validity = models.IntegerField(null=True, verbose_name='Срок действия',
                                   help_text='Срок действия типа РИД')
    renewal = models.IntegerField(null=True, verbose_name='Срок продления',
                                  help_text='Срок продления типа РИД')
    pay_period = models.IntegerField(null=True, verbose_name='Период оплаты',
                                     help_text='Период оплаты за тип РИД')

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
        verbose_name = 'страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.code


class Duty(models.Model):
    """Пошлина

    Поля:
        order_number Номер перечня
        name Наименование
        size Размер
        intellectual_property_type Типы РИД
    """

    order_number = models.CharField(max_length=50, null=True, verbose_name='Номер перечня',
                                    help_text='Номер перечня')
    name = models.CharField(max_length=250, null=True, verbose_name='Наименование',
                            help_text='Наименование пошлины')
    size = models.FloatField(null=True, verbose_name='Размер', help_text='Размер пошлины')
    intellectual_property_type = models.ManyToManyField(IntellectualPropertyType, verbose_name='Типы РИД',
                                                        help_text='Типы РИД, к которым относится пошлина.')

    class Meta:
        verbose_name = 'пошлина'
        verbose_name_plural = 'Пошлины'

    def __str__(self):
        return self.name


class IntellectualProperty(models.Model):
    """РИД

    Поля:
        name Название
        is_request Заявка
        request_number Номер заявки
        is_contracted Договор
        contract_number Номер договора
        contract_type Вид договора
        contract_date Дата заключения договора
        provider Исполнитель
        commissioner Руководитель
        text Тема
        number_policy_measure Номер программного мероприятия
        note Примечание
        protection_title Охранный документ
        abridgement Реферат
        ground Площадка СФУ
        type_fk Тип
        owners Патентообладатели
        creators Авторы
        countries Страны
        ipc МПК
        priority_date Дата приоритета
        send_date Дата подачи заявки
        grant_date Дата выдачи патента
        receipt_date Дата получения охраннового документа
        bulletin_number Номер бюллетеня
        bulletin_date Дата публикации бюллетеня
        duty_payments Оплаты пошлин
        is_supported Статус
    """

    # Заявка
    is_request = models.BooleanField(default=True, verbose_name='Заявка', help_text='Заявка ли?')
    request_number = models.IntegerField(verbose_name='Номер', null=True, blank=True,
                                         help_text='Номер заявки', validators=[MinValueValidator(0)])
    send_date = models.DateField(verbose_name='Дата подачи заявки', help_text='Дата подачи заявки')

    # Общие сведения
    name = models.CharField(max_length=200, blank=False, verbose_name='Название', help_text='Название РИД')
    type_fk = models.ForeignKey(to='IntellectualPropertyType', on_delete=models.PROTECT, verbose_name='Тип',
                                help_text='Тип РИД')
    ipc = models.CharField(max_length=1000, null=True, blank=True, default='', verbose_name='МПК',
                           help_text='Международная патентная классификация')
    text = models.TextField(verbose_name='Тема', help_text='Тема РИД', null=True, blank=True)
    abridgement = models.TextField(verbose_name='Реферат', null=True, blank=True, help_text='Реферат РИД')
    ground = models.ForeignKey(to='Ground', on_delete=models.PROTECT, verbose_name='Площадка СФУ',
                               help_text='Номер площадки СФУ')
    owners = models.ManyToManyField(Person, related_name='ip_owner', verbose_name='Патентообладатели',
                                    help_text='Патентообладатели РИД.')
    creators = models.ManyToManyField(Person, verbose_name='Авторы', help_text='Авторы РИД.')
    countries = models.ManyToManyField(Country, verbose_name='Страны',
                                       help_text='Страны, выдавшие патент.')
    note = models.TextField(verbose_name='Примечание', help_text='Примечание', null=True, blank=True)

    # Охранный документ
    protection_title = models.CharField(max_length=40, blank=True, null=True,
                                        verbose_name='Охранный документ',
                                        help_text='Номер охранного документа')
    priority_date = models.DateField(verbose_name='Дата приоритета', help_text='Дата регистрации РИД в ОФАП',
                                     null=True, blank=True)
    grant_date = models.DateField(verbose_name='Дата выдачи патента',
                                  help_text='Дата выдачи ФИПС охранного документа на РИД',
                                  blank=True, null=True)
    receipt_date = models.DateField(verbose_name='Дата получения охранного документа',
                                    help_text='Дата получения охранного документа отделом УИС',
                                    null=True, blank=True,)

    # Договор
    is_contracted = models.BooleanField(verbose_name='Договор', blank=True, default=False,
                                        help_text='Выполнено ли договору?')
    contract_number = models.CharField(max_length=50, blank=True, null=True, verbose_name='Номер договора',
                                       help_text='Номер договора')
    contract_type = models.ForeignKey(to='ContractType', blank=True, null=True, verbose_name='Вид договора',
                                      help_text='Вид договора', on_delete=models.PROTECT)
    contract_date = models.DateField(verbose_name='Дата заключения договора', null=True, blank=True,
                                     help_text='Дата заключения договора')
    provider = models.ForeignKey(to='Person', on_delete=models.PROTECT, related_name='provider',
                                 verbose_name='Исполнитель', help_text='Исполнитель', null=True, blank=True)
    commissioner = models.ForeignKey(to='Person', on_delete=models.PROTECT, related_name='commissioner',
                                     verbose_name='Руководитель', help_text='Руководитель', null=True, blank=True)
    number_policy_measure = models.CharField(max_length=50, verbose_name='Номер программного мероприятия',
                                             help_text='Номер программного мероприятия', null=True,
                                             blank=True)
    # Бюллетень
    bulletin_number = models.IntegerField(verbose_name='Номер бюллетеня', null=True, blank=True,
                                          validators=[MinValueValidator(1), MaxValueValidator(100)],
                                          help_text='Номер официального бюллетеня')
    bulletin_date = models.DateField(verbose_name='Дата публикации бюллетеня',
                                     help_text='Дата публикации официального бюллетеня',
                                     null=True, blank=True)
    # Оплата пошлин
    duty_payments = models.ManyToManyField(Duty, through='Payment', verbose_name='Оплаты пошлин',
                                           help_text='Пошлины к оплате за РИД.', blank=True)
    # Статус РИД
    is_supported = models.BooleanField(default=True, verbose_name='Статус', help_text='Поддерживается ли?')

    class Meta:
        verbose_name = 'РИД'
        verbose_name_plural = 'РИД'

    def __str__(self):
        if self.is_request:
            return 'Заявка на РИД с № (или id)' + str(self.request_number or self.id)
        return self.protection_title + ' - ' + self.name


class Payment(models.Model):
    """Оплаты пошлин

    Поля:
        duty Пошлина
        intellectual_property РИД
        purchase_order_number Номер платёжного поручения
        payment_date Дата оплаты
        posted_date Дата внесения
        paid_amount Сумма оплаты
        note Примечание
        check_scan Чек
    """

    duty = models.ForeignKey(Duty, on_delete=models.PROTECT, verbose_name='Пошлина',
                             help_text='Пошлина, за которую производится оплата')
    intellectual_property = models.ForeignKey(IntellectualProperty, on_delete=models.PROTECT,
                                              verbose_name='РИД',
                                              help_text='РИД, за который производится оплата')
    purchase_order_number = models.IntegerField(verbose_name='Номер платёжного поручения',
                                                help_text='Номер платёжного поручения')
    payment_date = models.DateField(verbose_name='Дата оплаты',
                                    help_text='Дата оплаты пошлины')
    posted_date = models.DateField(verbose_name='Дата внесения',
                                   help_text='Дата внесения оплаты пошлины')
    paid_amount = models.FloatField(verbose_name='Сумма оплаты',
                                    help_text='Сумма оплаты пошлины')
    note = models.TextField(verbose_name='Примечание', help_text='Примечание', null=True, blank=True)
    check_scan = models.ImageField(verbose_name='Чек', help_text='Скан чека', null=True, blank=True)

    class Meta:
        verbose_name = 'оплата пошлины'
        verbose_name_plural = 'Оплаты пошлин'

    def __str__(self):
        return str(self.purchase_order_number)


class IPCommercialization(models.Model):
    """Коммерциализация РИД

    Поля:
        intellectual_property РИД
        reference_number Номер дела
        send_date Дата отправки на регистрацию
        commercialization_type Наименование типа использования РИД
        licencee Лицензиат - получатель лицензии
        version_number Номер лицензионного договора на использование РИД
        filing_date Дата регистрации договора
        acceptance_delivery_acr Акт сдачи-приёмки
        contract_duration Срок действия договора
        agreement_terms Условия договора
        note Примечание
        licenser Лицензиары
    """

    intellectual_property = models.ForeignKey(to='IntellectualProperty', on_delete=models.PROTECT,
                                              verbose_name='РИД', help_text='РИД')
    reference_number = models.IntegerField(verbose_name='Номер дела', help_text='Номер дела')
    send_date = models.DateField(verbose_name='Дата отправки на регистрацию',
                                 help_text='Дата отправки на регистрацию')
    commercialization_type = models.ForeignKey(to='CommercializationType', on_delete=models.PROTECT,
                                               verbose_name='Наименование типа использования РИД',
                                               help_text='Наименование типа использования РИД')
    licencee = models.CharField(max_length=200, verbose_name='Лицензиат - получатель лицензии',
                                help_text='Лицензиат - получатель лицензии')
    version_number = models.CharField(max_length=50,
                                      verbose_name='Номер лицензионного договора на использование РИД',
                                      help_text='Номер лицензионного договора на использование РИД')
    filing_date = models.DateField(verbose_name='Дата регистрации договора',
                                   help_text='Дата регистрации договора')
    acceptance_delivery_acr = models.BooleanField(verbose_name='Акт сдачи-приёмки',
                                                  help_text='Акт сдачи-приёмки')
    contract_duration = models.CharField(max_length=100, verbose_name='Срок действия договора',
                                         help_text='Срок действия договора')
    agreement_terms = models.TextField(verbose_name='Условия договора', help_text='Условия договора', null=True, blank=True)
    note = models.TextField(verbose_name='Примечание', help_text='Примечание', null=True, blank=True)
    licenser = models.ManyToManyField(Person, verbose_name='Лицензиары', help_text='Лицензиары.')

    class Meta:
        verbose_name = 'коммерциализация РИД'
        verbose_name_plural = 'Коммерциализация РИД'

    def __str__(self):
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

    intellectual_property = models.ForeignKey(to='IntellectualProperty', on_delete=models.PROTECT,
                                              verbose_name='РИД', help_text='РИД')
    date = models.DateField(verbose_name='Дата постановки на НМА',
                            help_text='Дата поставки на НМА')
    number = models.CharField(max_length=10, verbose_name='Номер акта',
                              help_text='Номер акта')
    book_value = models.FloatField(verbose_name='Балансовая стоимость',
                                   help_text='Балансовая стоимость')
    retirement_date = models.DateField(verbose_name='Дата списания', help_text='Дата списания', null=True, blank=True)

    class Meta:
        verbose_name = 'запись реестра НМА'
        verbose_name_plural = 'Реестр НМА'

    def __str__(self):
        return str(self.intellectual_property)


class CardRegister(models.Model):
    """Картотека

    Поля:
        intellectual_property РИД
        status Статус
        refusal_date Дата отказа поддержки
        note Примечание
    """

    intellectual_property = models.ForeignKey(to='IntellectualProperty', on_delete=models.PROTECT,
                                              verbose_name='РИД', help_text='РИД')
    status = models.CharField(max_length=200, verbose_name='Статус',
                              help_text='Статус')
    refusal_date = models.DateField(verbose_name='Дата отказа поддержки',
                                    help_text='Дата отказа поддержки')
    note = models.TextField(verbose_name='Примечание', help_text='Примечание')

    class Meta:
        verbose_name = 'запись картотеки'
        verbose_name_plural = 'Картотека'

    def __str__(self):
        return str(self.intellectual_property)


class PrivatePerson(Person):
    """Автор

    Поля:
        surname Фамилия
        name Имя
        patronymic Отчество
        work_place Подразделения СФУ - место работы
        passport_series Серия паспорта
        passport_number Номер паспорта
    """

    surname = models.CharField(max_length=100, blank=False, verbose_name='Фамилия',
                               help_text='Фамилия автора. Например, Нурлыгаянов')
    name = models.CharField(max_length=100, blank=False, verbose_name='Имя',
                            help_text='Имя автора. Например, Никита')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество',
                                  help_text='Отчество автора. Например, Рамильевич')
    work_place = models.CharField(max_length=100, blank=False,
                                  verbose_name='Институт СФУ — место работы',
                                  help_text='Институт СФУ — место работы автора. Например, ИКИТ')
    passport_series = models.CharField(max_length=15, verbose_name='Серия паспорта',
                                       help_text='Серия паспорта автора', validators=[MinLengthValidator(4)])
    passport_number = models.CharField(max_length=15, verbose_name='Номер паспорта',
                                       help_text='Номер паспорта автора', validators=[MinLengthValidator(6)])

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'Авторы'
        unique_together = ('passport_series', 'passport_number')

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

    name = models.CharField(max_length=200, blank=False, null=True, verbose_name='Наименование',
                            help_text='Наименование юридического лица')
    address = models.CharField(max_length=200, blank=False, null=True, verbose_name='Физический адрес',
                               help_text='Физический адрес юридического лица')
    phone = models.CharField(max_length=100, blank=False, null=True, verbose_name='Телефонный номер',
                             help_text='Телефонный номер юридического лица. Например, +78005553535')
    fax = models.CharField(max_length=100, blank=False, null=True, verbose_name='Факс',
                           help_text='Факс юридического лица')
    site = models.CharField(max_length=100, blank=False, null=True, verbose_name='Адрес сайта',
                            help_text='Адрес сайта юридического лиц')
    email = models.CharField(max_length=100, blank=False, null=True, verbose_name='Адрес электронной почты',
                             help_text='Адрес электронной почты юридического лица')

    class Meta:
        verbose_name = 'юридическое лицо'
        verbose_name_plural = 'Юридические лица'

    def __str__(self):
        return self.name


NOTIFICATION_TYPE_CHOICES = (
    ('delete', 'Удаление'),
    ('update', 'Редактирование'),
    ('create', 'Добавление'),
)


class Notification(models.Model):
    time = models.DateTimeField(verbose_name="Время произошедшего события")
    type = models.CharField(verbose_name='Тип события', max_length=100, choices=NOTIFICATION_TYPE_CHOICES)
    description = models.TextField(verbose_name='Описание события')
    read = models.BooleanField(verbose_name='Просмотрено ли событие', default=False)
