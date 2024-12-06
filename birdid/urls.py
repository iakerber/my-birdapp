from django.urls import path
from . import views

urlpatterns = [
    path('', views.waterbird_list, name='waterbird_list'),
]