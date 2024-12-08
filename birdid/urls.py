from django.urls import path
from . import views

urlpatterns = [
    path('', views.waterbird_list, name='waterbird_list'),
    path('waterbird/<int:pk>/', views.waterbird_detail, name='waterbird_detail'),
]