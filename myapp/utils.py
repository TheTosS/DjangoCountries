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
<<<<<<< HEAD
        if country['country'].lower() == name.lower():
=======
        if country['name'].lower() == name.lower():
>>>>>>> 875e986d4b38cb490cd3c20f313159aa7ee76d8d
            return country
    return None