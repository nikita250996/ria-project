from django.db import models
from django.contrib.auth.models import User

# Пользователи системы
class Employees(models.Model):
    # Использованы в User
    # name = models.CharField(max_length=100, blank=False)
    # surname = models.CharField(max_length=100)
    # email = models.CharField(max_length=100, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ground = models.ForeignKey(to='Ground', on_delete=models.PROTECT, null=True)
    patronymic = models.CharField(max_length=100, null=True)
    jobrole = models.CharField(max_length=100, null=True)
    # поменял на 200
    home_address = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(null=True)

    mobile_phone = models.CharField(max_length=20, null=True)
    home_phone = models.CharField(max_length=20, null=True)


# Тип коммерциализации РИД
#   name - наименование использования РИД
class CommercializationType(models.Model):
    name = models.CharField(max_length=100, blank=False)

# Тип договора на РИД
#   name - вид договора
class ContractType(models.Model):
    name = models.CharField(max_length=100, blank=False)

# Площадки
#   phone - телефон площадки
#   index - индекс площадки
#   address - адрес площадки
class Ground(models.Model):
    ground_code = models.IntegerField(unique=True)
    phone = models.CharField(max_length=50, null=True)
    index = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, blank=False, null=True)

# Типы РИД
#   name - наименование типа РИД
#
class IntellectualPropertyType(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    protection_document_name = models.CharField(max_length=100, blank=False, null=True)
    validity = models.IntegerField(null=True)
    renewal = models.IntegerField(null=True)
    pay_period = models.IntegerField(null=True)

class Person(models.Model):
    # class Meta:
    #     abstract = True
    pass


class IPC(models.Model):
    index = models.CharField(max_length=50)
    description = models.TextField()

class Country(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100, blank=False)

class Request(models.Model):
    number = models.IntegerField()
    protection_title = models.CharField(max_length=40, blank=False)
    # request_ip_name
    ip_name = models.CharField(max_length=200, blank=False)
    abridgement = models.TextField()
    ground = models.ForeignKey(to='Ground', on_delete=models.PROTECT)
    ip_type = models.ForeignKey(to='IntellectualPropertyType', on_delete=models.PROTECT)
    ipc = models.IntegerField()
    bulletin_number = models.IntegerField()
    bulletin_date = models.DateTimeField()
    priority_date = models.DateTimeField()
    send_date = models.DateTimeField()
    receipt_date = models.DateTimeField()
    grant_date = models.DateTimeField()
    is_contracted = models.BooleanField()
    contract_number = models.CharField(max_length=50)
    contract_date = models.DateTimeField()
    text = models.TextField()
    number_policy_measure = models.CharField(max_length=50)
    note = models.TextField()
    contract_type = models.ForeignKey(to='ContractType', on_delete=models.PROTECT)
    provider = models.ForeignKey(to='Person', on_delete=models.PROTECT, related_name='provider')
    commissioner = models.ForeignKey(to='Person', on_delete=models.PROTECT, related_name='commissioner')
    owner = models.ManyToManyField(Person, related_name='ip_owner')
    creator = models.ManyToManyField(Person)
    ipc = models.ManyToManyField(IPC)
    country = models.ManyToManyField(Country)

class Duty(models.Model):
    order_number = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=250, null=True)
    size = models.FloatField(null=True)
    intellectual_property_type = models.ManyToManyField(IntellectualPropertyType)

class IntellectualProperty(models.Model):
    # номер заявки
    # НомЗаявки
    request_number = models.IntegerField()
    # номер - охранный документ
    # НомОхрДок
    protection_title = models.CharField(max_length=40)
    # название РИД
    # НазвРИД
    name = models.CharField(max_length=200, blank=False)
    # реферат
    # Реферат
    abridgement = models.TextField()
    # Код площадки
    # КодПл
    ground = models.ForeignKey(to='Ground', on_delete=models.PROTECT)
    # тип РИД
    # КодТипаРИД
    type_fk = models.ForeignKey(to='IntellectualPropertyType', on_delete=models.PROTECT)
    # номер бюллетени
    # НомБюл
    bulletin_number = models.IntegerField()
    #
    #
    bulletin_date = models.DateField()
    #
    #
    priority_date = models.DateField()
    # Дата получения охранного документа
    #
    grant_date = models.DateField()
    #
    #
    duty_payments = models.ManyToManyField(Duty, through='Payment')

class Payment(models.Model):
    duty = models.ForeignKey(Duty, on_delete=models.PROTECT)
    intellectual_property = models.ForeignKey(IntellectualProperty, on_delete=models.PROTECT)
    purchase_order_number = models.IntegerField()
    payment_date = models.DateField()
    posted_date = models.DateField()
    paid_amount = models.FloatField()
    note = models.TextField()

class ContractIntellectualProperties(models.Model):
    intellectual_property = models.ForeignKey(to='IntellectualProperty', on_delete=models.PROTECT)
    number = models.CharField(max_length=50)
    date = models.DateField()
    text = models.TextField()
    number_policy_measure = models.CharField(max_length=50)
    note = models.TextField()
    contract_type = models.ForeignKey(to='ContractType', on_delete=models.PROTECT)
    provider = models.ForeignKey(to='Person', on_delete=models.PROTECT, related_name='prov')
    commissioner = models.ForeignKey(to='Person', on_delete=models.PROTECT, related_name='comm')

class IntellectualPropertyCommercialization(models.Model):
    intellectual_property = models.ForeignKey(to='IntellectualProperty', on_delete=models.PROTECT)
    reference_number = models.IntegerField()
    send_date = models.DateField()
    commercialization_type = models.ForeignKey(to='CommercializationType', on_delete=models.PROTECT)
    licencee = models.CharField(max_length=200)
    version_number = models.CharField(max_length=50)
    filing_date = models.DateField()
    acceptance_delivery_acr = models.BooleanField()
    contract_duration = models.CharField(max_length=100)
    agreement_terms = models.TextField()
    note = models.TextField()
    licenser = models.ManyToManyField(Person)

class IntangibleAssets(models.Model):
    intellectual_property = models.ForeignKey(to='IntellectualProperty', on_delete=models.PROTECT)
    date = models.DateField()
    number = models.CharField(max_length=10)
    book_value = models.FloatField()
    retirement_date = models.DateField()

class CardRegister(models.Model):
    intellectual_property = models.ForeignKey(to='IntellectualProperty', on_delete=models.PROTECT)
    status = models.CharField(max_length=200)
    refusal_date = models.DateField()
    note = models.TextField()



class PrivatePerson(Person):
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    patronymic = models.CharField(max_length=100)
    work_place = models.CharField(max_length=100, blank=False)

    def full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

class LegalPerson(Person):
    name = models.CharField(max_length=200, blank=False, null=True)
    address = models.CharField(max_length=200, blank=False, null=True)
    phone = models.CharField(max_length=100, blank=False, null=True)
    fax = models.CharField(max_length=100, blank=False, null=True)
    site = models.CharField(max_length=100, blank=False, null=True)
    email = models.CharField(max_length=100, blank=False, null=True)
