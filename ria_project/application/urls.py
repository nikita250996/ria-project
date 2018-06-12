# coding: utf-8
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('',
         login_required(TemplateView.as_view(template_name='index.html')),
         name='index'),

    path('рид',
         login_required(TemplateView.as_view(template_name='intellectual_properties.html')),
         name='intellectual_properties'),

    path('рид-по-договорам',
         login_required(TemplateView.as_view(template_name='contract_intellectual_properties.html')),
         name='contract_intellectual_properties'),

    path('нематериальные-активы',
         login_required(TemplateView.as_view(template_name='intangible_assets.html')),
         name='intangible_assets'),

    path('оплаты-пошлин',
         login_required(TemplateView.as_view(template_name='payments.html')),
         name='payments'),

    path('коммерциализация-рид',
         login_required(TemplateView.as_view(template_name='intellectual_properties_commercialization.html')),
         name='intellectual_properties_commercialization'),

    path('отчеты',
         login_required(TemplateView.as_view(template_name='statistics.html')),
         name='statistics'),
]


urlpatterns += [
    path('заявки/добавить', views.RequestCreate.as_view(), name='request_intellectual_property_create'),
    path('заявки/<int:pk>/редактировать/', views.RequestUpdate.as_view(), name='request_intellectual_property_update'),

    path('рид/<int:pk>/редактировать/', views.IPUpdate.as_view(), name='intellectual_property_update'),

    path('рид-по-договорам/<int:pk>/редактировать/', views.IPContractUpdate.as_view(),
         name='contract_intellectual_property_update'),
]

urlpatterns += [
    path('нематериальные-активы/добавить',
         views.IntAssetCreate.as_view(), name='intangible_assets_create'),
    path('нематериальные-активы/<int:pk>/редактировать',
         views.IntAssetUpdate.as_view(), name='intangible_assets_update'),
]

urlpatterns += [
    path('оплаты-пошлин/добавить', views.PaymentCreate.as_view(), name='payment_create'),
    path('оплаты-пошлин/<int:pk>/редактировать', views.PaymentUpdate.as_view(), name='payment_update'),
]

urlpatterns += [
    path('коммерциализация-рид/добавить',
         views.IPCommercializationCreate.as_view(), name='intellectual_properties_commercialization_create'),
    path('коммерциализация-рид/<int:pk>/редактировать',
         views.IPCommercializationUpdate.as_view(), name='intellectual_properties_commercialization_update'),
]

urlpatterns += [
    path('сообщения/входящие',
         login_required(TemplateView.as_view(template_name='received_messages.html')),
         name='received_messages'),
    path('сообщения/написать', views.MessageCreate.as_view(), name='message_create'),
    path('сообщения/входящие/<int:pk>/ответить', views.MessageRead.as_view(), name='message_read'),
    path('сообщения/исходящие/<int:pk>/', views.MessageOpen.as_view(), name='message_open'),
    path('сообщения/исходящие',
         login_required(TemplateView.as_view(template_name='sent_messages.html')),
         name='sent_messages'),
]