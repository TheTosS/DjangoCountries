import json
import os
from django.conf import settings

def load_countries():
    file_path = os.path.join(settings.BASE_DIR, 'countries.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_country_by_name(name):
    countries = load_countries()
    for country in countries:
        if country['country'].lower() == name.lower():
            return country
    return None