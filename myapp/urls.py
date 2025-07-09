from django.urls import path
from . import views  # Импорт ваших представлений
from .views import countries_list, country_detail
from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('countries-list/', countries_list, name='countries_list'),
    path("country/<str:country_name>/", country_detail, name='country_detail'),
    path('languages/', views.languages_list, name='languages'),
]