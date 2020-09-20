from django.urls import path

app_name = 'core'

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar/', views.search_tasks, name='search_tasks'),
]