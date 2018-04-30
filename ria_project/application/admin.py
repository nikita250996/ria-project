from django.contrib import admin
from application.models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class CommercializationTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

class GroundAdmin(admin.ModelAdmin):
    list_display = ('ground_code', 'phone', 'index', 'address')

class IntellectualPropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'protection_document_name', 'validity', 'renewal', 'pay_period')

class IPCAdmin(admin.ModelAdmin):
    list_display = ('index', 'description')

# Нужно получать ещё name, surname, email
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('user', 'ground', 'patronymic', 'jobrole', 'jobrole', 'birth_date', 'mobile_phone', 'home_phone')

# Нужно получать ещё ipc, owner, creator, country
class RequestAdmin(admin.ModelAdmin):
    list_display = ('number', 'protection_title', 'ip_name', 'abridgement', 'ground', 'ip_type', 'bulletin_number', 'bulletin_date', 'priority_date', 'send_date', 'receipt_date', 'grant_date', 'is_contracted', 'contract_number', 'contract_date', 'text', 'number_policy_measure', 'note', 'contract_type', 'provider', 'commissioner')

# Нужно получать ещё intellectual_property_type
class DutyAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'name', 'size')

# Нужно получать ещё duty_payments
class IntellectualPropertyAdmin(admin.ModelAdmin):
    list_display = ('request_number', 'protection_title', 'name', 'abridgement', 'ground', 'type_fk', 'bulletin_number', 'bulletin_date', 'priority_date', 'grant_date')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('duty', 'intellectual_property', 'purchase_order_number', 'payment_date', 'posted_date', 'paid_amount', 'note')

class ContractIntellectualPropertiesAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'number', 'date', 'text', 'number_policy_measure', 'note', 'contract_type', 'provider', 'commissioner')

# Нужно получать ещё licenser
class IntellectualPropertyCommercializationAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'reference_number', 'send_date', 'commercialization_type', 'licencee', 'version_number', 'filing_date', 'acceptance_delivery_acr', 'contract_duration', 'agreement_terms', 'note')

class IntangibleAssetsAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'date', 'number', 'book_value', 'retirement_date')

class CardRegisterAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'status', 'refusal_date', 'note')

class PrivatePersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'work_place')

class LegalPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'fax', 'site', 'email')

# Зарегистрированные модели
admin.site.register(Country, CountryAdmin)
admin.site.register(CommercializationType, CommercializationTypeAdmin)
admin.site.register(ContractType, ContractTypeAdmin)
admin.site.register(Ground, GroundAdmin)
admin.site.register(IntellectualPropertyType, IntellectualPropertyTypeAdmin)
admin.site.register(IPC, IPCAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(IntellectualProperty, IntellectualPropertyAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(ContractIntellectualProperties, ContractIntellectualPropertiesAdmin)
admin.site.register(IntellectualPropertyCommercialization, IntellectualPropertyCommercializationAdmin)
admin.site.register(IntangibleAssets, IntangibleAssetsAdmin)
admin.site.register(CardRegister, CardRegisterAdmin)
admin.site.register(PrivatePerson, PrivatePersonAdmin)
admin.site.register(LegalPerson, LegalPersonAdmin)
# Что-то тут не очень :(
admin.site.register(Person)
