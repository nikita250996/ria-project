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


# TODO Нужно получать ещё ipc
class RequestAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     ('Библиографические данные', {
    #         'classes': ('extrapretty'),
    #         'fields': (
    #             ('number', 'protection_title',),
    #             ('send_date', 'priority_date',), ('grant_date', 'receipt_date',),
    #             ('provider', 'commissioner'),
    #             ('creators', 'owners', 'countries')
    #         )
    #     }),
    #     ('Описание', {
    #         'classes': (),
    #         'fields': (
    #             ()
    #         ),
    #     }),
    #     ('Договор', {
    #         'classes': ('collapse',),
    #         'fields': ('is_contracted', 'contract_number', 'contract_type', 'contract_date',)
    #     }),
    # )

    list_display = [
        'number', 'protection_title', 'ip_name', 'abridgement', 'ground', 'ip_type', 'bulletin_number',
        'bulletin_date', 'priority_date', 'send_date', 'receipt_date', 'grant_date',
        'is_contracted', 'contract_number', 'contract_date', 'text', 'number_policy_measure',
        'note', 'contract_type',
        'provider', 'commissioner', 'get_owners', 'get_creators', 'get_countries'
    ]

    def get_countries(self, obj):
        return ", ".join([str(country) for country in obj.countries.all()])
    get_countries.short_description = 'Страны'

    def get_owners(self, obj):
        return "; ".join(
            [str(owner) for owner in obj.owners.all()]
        )
    get_owners.short_description = 'Патентообладатели'

    def get_creators(self, obj):
        return "; ".join([str(creator) for creator in obj.creators.all()])
    get_creators.short_description = 'Авторы'



# TODO Разделить ТипыРИД на два слова
class DutyAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'name', 'ТипыРИД')

    def ТипыРИД(self, obj):
        return ", ".join([str(intellectual_property_type) for intellectual_property_type in obj.intellectual_property_type.all()])


# Для IntellectualPropertyAdmin
class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


# TODO Разделить Оплатыпошлины на два слова
class IntellectualPropertyAdmin(admin.ModelAdmin):
    inlines = (PaymentInline,)
    list_display = ('request_number', 'protection_title', 'name', 'abridgement', 'ground', 'type_fk', 'bulletin_number', 'bulletin_date', 'priority_date', 'grant_date', 'Оплатыпошлины')

    def Оплатыпошлины(self, obj):
        return ", ".join([str(duty_payment) for duty_payment in obj.duty_payments.all()])


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('duty', 'intellectual_property', 'purchase_order_number', 'payment_date', 'posted_date', 'paid_amount', 'note')


class ContractIntellectualPropertiesAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'number', 'date', 'text', 'number_policy_measure', 'note', 'contract_type', 'provider', 'commissioner')


class IntellectualPropertyCommercializationAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'reference_number', 'send_date', 'commercialization_type', 'licencee', 'version_number', 'filing_date', 'acceptance_delivery_acr', 'contract_duration', 'agreement_terms', 'note', 'Лицензиары')

    def Лицензиары(self, obj):
        return ", ".join([str(licenser) for licenser in obj.licenser.all()])


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
admin.site.register(IPCommercialization, IntellectualPropertyCommercializationAdmin)
admin.site.register(IntangibleAssets, IntangibleAssetsAdmin)
admin.site.register(CardRegister, CardRegisterAdmin)
admin.site.register(PrivatePerson, PrivatePersonAdmin)
admin.site.register(LegalPerson, LegalPersonAdmin)
# admin.site.register(Person)
