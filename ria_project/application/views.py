from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# заявки
@login_required
def index(request):
    return render(request, 'index.html')


# рид
@login_required
def intellectual_properties(request):
    return render(request, 'intellectual_properties.html')


# рид по договорам
@login_required
def contract_intellectual_properties(request):
    return render(request, 'contract_intellectual_properties.html')


# охранные документы
@login_required
def protection_titles(request):
    return render(request, 'protection_titles.html')


# нма
@login_required
def intangible_assets(request):
    return render(request, 'intangible_assets.html')


# пошлины
@login_required
def duties(request):
    return render(request, 'duties.html')


# коммерциализация рид
@login_required
def intellectual_properties_commercialization(request):
    return render(request, 'intellectual_properties_commercialization.html')


# отчеты/реестры
@login_required
def statistics(request):
    return render(request, 'statistics.html')
