from django.shortcuts import render
from django.http import HttpResponse


# заявки
def index(request):
    return render(request, 'index.html')


# рид
def intellectual_properties(request):
    return render(request, 'intellectual_properties.html')


# рид по договорам
def contract_intellectual_properties(request):
    return render(request, 'contract_intellectual_properties.html')


# охранные документы
def protection_titles(request):
    return render(request, 'protection_titles.html')


# нма
def intangible_assets(request):
    return render(request, 'intangible_assets.html')


# пошлины
def duties(request):
    return render(request, 'duties.html')


# коммерциализация рид
def intellectual_properties_commercialization(request):
    return render(request, 'intellectual_properties_commercialization.html')


# отчеты/реестры
def statistics(request):
    return render(request, 'statistics.html')
