# coding: utf-8
from django.contrib import admin
from application.models import *
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin


# авторы
class PrivatePersonAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'work_place', 'passport_series', 'passport_number')


# картотека
class CardRegisterAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'status', 'refusal_date', 'note')


# коммерциализация РИД
class IntellectualPropertyCommercializationAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'reference_number', 'send_date', 'commercialization_type',
                    'licencee', 'version_number', 'filing_date', 'acceptance_delivery_acr', 'contract_duration',
                    'agreement_terms', 'note', 'get_licensers')

    def get_licensers(self, obj):
        return "; ".join([str(licenser) for licenser in obj.licenser.all()])
    get_licensers.short_description = 'Лицензиары'


# оплаты пошлин
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('duty', 'intellectual_property', 'purchase_order_number', 'payment_date', 'posted_date',
                    'paid_amount', 'note', 'check_scan_image')

    def check_scan_image(self, obj):
        if obj.check_scan and hasattr(obj, 'check_scan'):
            return mark_safe('<a href={url} target="_blank"><img src="{url}" width="{width}" height={height}"></a>'
                .format(url=obj.check_scan.url, width=64, height=64,)
            )
        return "Нет чека"
    check_scan_image.short_description = 'Скан чека'


# площадки СФУ
class GroundAdmin(admin.ModelAdmin):
    list_display = ('ground_code', 'phone', 'index', 'address')


# пользователи
class PageAdmin(UserAdmin):
    # list_display = ('username', 'password', 'first_name', 'last_name', 'patronymic', 'email')
    pass


# пошлины
class DutyAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'name', 'size', 'get_ip_types')

    def get_ip_types(self, obj):
        return "; ".join([str(intellectual_property_type) for intellectual_property_type in obj.intellectual_property_type.all()])
    get_ip_types.short_description = 'Типы РИД'


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


# РИД
class IntellectualPropertyAdmin(admin.ModelAdmin):
    inlines = (PaymentInline,)
    list_display = (
        'name', 'class_fication', 'is_request', 'request_number', 'is_contracted', 'contract_number', 'contract_type',
        'contract_date', 'provider', 'commissioner', 'text', 'number_policy_measure', 'note', 'protection_title',
        'abridgement', 'ground', 'type_fk', 'get_owners', 'get_creators', 'get_countries', 'ipc',
        'priority_date', 'send_date', 'grant_date', 'receipt_date', 'bulletin_number', 'bulletin_date',
        'get_duty_payments', 'is_supported',)

    def get_owners(self, obj):
        return "; ".join(
            [str(owner) for owner in obj.owners.all()]
        )
    get_owners.short_description = 'Патентообладатели'

    def get_creators(self, obj):
        return "; ".join([str(creator) for creator in obj.creators.all()])
    get_creators.short_description = 'Авторы'

    def get_countries(self, obj):
        return "; ".join([str(country) for country in obj.countries.all()])
    get_countries.short_description = 'Страны'

    def get_duty_payments(self, obj):
        return "; ".join([str(duty_payment) for duty_payment in obj.duty_payments.all()])
    get_duty_payments.short_description = 'Оплаты пошлин'


# реестр НМА
class IntangibleAssetsAdmin(admin.ModelAdmin):
    list_display = ('intellectual_property', 'date', 'number', 'book_value', 'retirement_date')


# сотрудники УИС
class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'ground', 'jobrole', 'birth_date', 'mobile_phone', 'home_address', 'home_phone')


# страны
class CountryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


# типы РИД
class IntellectualPropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'protection_document_name', 'validity', 'renewal', 'pay_period')


# типы договора на РИД
class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


# типы коммерциализации РИД
class CommercializationTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


# юридические лица
class LegalPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'fax', 'site', 'email')


# сообщения
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'text', 'send_at', 'read')


# институты
class InstituteAdmin(admin.ModelAdmin):
    list_display = ('name', 'ground')


admin.site.site_header = 'РИД СФУ'
admin.site.index_template = './admin/index.html'
admin.site.index_title = 'Главная'
admin.site.site_title = 'Панель администратора'

# Зарегистрированные модели
admin.site.register(PrivatePerson, PrivatePersonAdmin)
admin.site.register(CardRegister, CardRegisterAdmin)
admin.site.register(IPCommercialization, IntellectualPropertyCommercializationAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Ground, GroundAdmin)
admin.site.register(User, PageAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(IntellectualProperty, IntellectualPropertyAdmin)
admin.site.register(IntangibleAssets, IntangibleAssetsAdmin)
admin.site.register(EmployeeInfo, EmployeeInfoAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(IntellectualPropertyType, IntellectualPropertyTypeAdmin)
admin.site.register(ContractType, ContractTypeAdmin)
admin.site.register(CommercializationType, CommercializationTypeAdmin)
admin.site.register(LegalPerson, LegalPersonAdmin)

admin.site.register(PaymentInfo)
admin.site.register(ClassificationGroup)
admin.site.register(Classification)

admin.site.register(Message, MessageAdmin)
admin.site.register(Institute, InstituteAdmin)
