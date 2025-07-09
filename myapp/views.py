

from django.views.generic import TemplateView
import json
import os
from django.conf import settings
from django.shortcuts import render
from .utils import load_countries, get_country_by_name
from django.http import Http404


class HomeView(TemplateView):
    template_name = 'myapp/index.html'


def countries_list(request):
    countries = load_countries()
    return render(request, 'myapp/countries_list.html', {'countries': countries})

def country_detail(request, country_name):
    country = get_country_by_name(country_name)
    if not country:
        raise Http404("Страна не найдена")
    return render(request, 'myapp/country_detail.html', {'country': country})

# Create your views here.
