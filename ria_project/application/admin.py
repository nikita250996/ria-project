from django.contrib import admin
from django.contrib.admin import AdminSite
from application.models import *
from django.utils.safestring import mark_safe


class PageAdmin(admin.ModelAdmin):
    # list_display = ('username', 'password', 'first_name', 'last_name', 'patronymic', 'email')
    pass

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


class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'ground', 'jobrole', 'birth_date', 'mobile_phone', 'home_phone')


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
        'number', 'protection_title', 'ip_name', 'abridgement', 'ground', 'ip_type', 'ipc',
        'bulletin_number', 'bulletin_date', 'priority_date', 'send_date', 'receipt_date', 'grant_date',
        'is_contracted', 'contract_type', 'contract_number', 'contract_date', 'text', 'number_policy_measure',
        'note', 'provider', 'commissioner', 'get_owners', 'get_creators', 'get_countries'
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


class DutyAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'name', 'get_ip_types')

    def get_ip_types(self, obj):
        return ", ".join([str(intellectual_property_type) for intellectual_property_type in obj.intellectual_property_type.all()])
    get_ip_types.short_description = 'Типы РИД'


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


class IntellectualPropertyAdmin(admin.ModelAdmin):
    inlines = (PaymentInline,)
    list_display = ('ipc', 'request_number', 'protection_title', 'name', 'abridgement', 'ground', 'type_fk',
                    'bulletin_number', 'bulletin_date', 'priority_date', 'grant_date', 'duty_payment')

    def duty_payment(self, obj):
        return ", ".join([str(duty_payment) for duty_payment in obj.duty_payments.all()])
    duty_payment.short_description = 'Оплаты пошлин'


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('duty', 'intellectual_property', 'purchase_order_number', 'payment_date', 'posted_date',
                    'paid_amount', 'note', 'check_scan_image')

    def check_scan_image(self, obj):
        return mark_safe('<a href={url} target="_blank"><img src="{url}" width="{width}" height={height}"></a>'.format(
            url=obj.check_scan.url,
            width=64,
            height=64,
        )
    )
    check_scan_image.short_description = 'Скан чека'


class ContractIntellectualPropertiesAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'number', 'date', 'text', 'number_policy_measure', 'note',
                    'contract_type', 'provider', 'commissioner')


class IntellectualPropertyCommercializationAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'reference_number', 'send_date', 'commercialization_type',
                    'licencee', 'version_number', 'filing_date', 'acceptance_delivery_acr', 'contract_duration',
                    'agreement_terms', 'note', 'get_licensers')

    def get_licensers(self, obj):
        return ", ".join([str(licenser) for licenser in obj.licenser.all()])
    get_licensers.short_description = 'Лицензиары'


class IntangibleAssetsAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'date', 'number', 'book_value', 'retirement_date')


class CardRegisterAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'status', 'refusal_date', 'note')


class PrivatePersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'work_place')


class LegalPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'fax', 'site', 'email')


admin.site.site_header = 'РИД СФУ'
admin.site.index_template = './admin/index.html'
admin.site.index_title = 'Главная'
admin.site.site_title = 'Панель администратора'

# Зарегистрированные модели
admin.site.register(User, PageAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(CommercializationType, CommercializationTypeAdmin)
admin.site.register(ContractType, ContractTypeAdmin)
admin.site.register(Ground, GroundAdmin)
admin.site.register(IntellectualPropertyType, IntellectualPropertyTypeAdmin)
admin.site.register(EmployeeInfo, EmployeeInfoAdmin)
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
