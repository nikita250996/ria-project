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

    path('охранные-документы',
         login_required(TemplateView.as_view(template_name='protection_titles.html')),
         name='protection_titles'),

    path('нематериальные-активы',
         login_required(TemplateView.as_view(template_name='intangible_assets.html')),
         name='intangible_assets'),

    path('оплаты-пошлин',
         login_required(TemplateView.as_view(template_name='payments.html')),
         name='payments'),

    path('коммерциализация',
         login_required(TemplateView.as_view(template_name='intellectual_properties_commercialization.html')),
         name='intellectual_properties_commercialization'),

    path('отчеты',
         login_required(TemplateView.as_view(template_name='statistics.html')),
         name='statistics'),
]

urlpatterns += [
    path('заявки/добавить-заявку', views.RequestCreate.as_view(), name='request_create'),
    path('заявки/<int:pk>/редактировать-заявку', views.RequestUpdate.as_view(), name='request_update'),
]