from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('рид', views.intellectual_properties, name='intellectual_properties'),
    path('рид-по-договорам', views.contract_intellectual_properties, name='contract_intellectual_properties'),
    path('охранные-документы', views.protection_titles, name='protection_titles'),
    path('нематериальные-активы', views.intangible_assets, name='intangible_assets'),
    path('пошлины', views.duties, name='duties'),
    path('коммерциализация', views.intellectual_properties_commercialization, name='intellectual_properties_commercialization'),
    path('отчеты', views.statistics, name='statistics'),
]
