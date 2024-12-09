from django.urls import path
from . import views

urlpatterns = [
    path('', views.waterbird_list, name='waterbird_list'),
    path('waterbird/<int:pk>/', views.waterbird_detail, name='waterbird_detail'),
    path('waterbird/new/', views.waterbird_new, name='waterbird_new'),
    path('waterbird/<int:pk>/edit/', views.waterbird_edit, name='waterbird_edit'),
]