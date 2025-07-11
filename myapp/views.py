

from django.views.generic import TemplateView
import json

from django.shortcuts import render
from django.conf import settings
import os
from .utils import load_countries, get_country_by_name
from django.http import Http404


class HomeView(TemplateView):
    template_name = 'myapp/index.html'

import os
from django.conf import settings
from django.shortcuts import render
from .utils import load_countries, get_country_by_name
from django.http import Http404



class HomeView(TemplateView):
    template_name = 'myapp/index.html'

def countries_list(request):
    # Получаем путь к файлу countries.json
    json_path = os.path.join(settings.BASE_DIR, 'countries.json')


    # Загружаем данные из JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        countries_data = json.load(f)

    # Извлекаем только названия стран
    country_names = [country['country'] for country in countries_data]

    # Передаем данные в шаблон
    context = {
        'countries': country_names
    }
    return render(request, 'myapp/countries_list.html', context)


def countries_list(request):
    countries = load_countries()
    return render(request, 'myapp/countries_list.html', {'countries': countries})


def country_detail(request, country_name):
    country = get_country_by_name(country_name)
    if not country:
        raise Http404("Страна не найдена")
    return render(request, 'myapp/country_detail.html', {'country': country })

# Create your views here.



    # Собираем все уникальные языки


def languages_list(request):
    # Чтение данных из countries.json
    with open('countries.json', 'r', encoding='utf-8') as f:
        countries_data = json.load(f)

    # Собираем все уникальные языки
    languages = set()
    for country in countries_data:
        for lang in country['languages']:
            languages.add(lang)

    return render(request, 'myapp/languages.html', {'languages': sorted(languages)})