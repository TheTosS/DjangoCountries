from django.urls import path
from . import views  # Импорт ваших представлений

urlpatterns = [
    path('', views.home_view, name='home'),
    # Добавьте другие пути по необходимости
]