from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('waterbird/list/', views.waterbird_list, name='waterbird_list'),
    path('waterbird/<int:pk>/', views.waterbird_detail, name='waterbird_detail'),
    path('waterbird/new/', views.waterbird_new, name='waterbird_new'),
    path('waterbird/<int:pk>/edit/', views.waterbird_edit, name='waterbird_edit'),
    
    path('raptor/list/', views.raptor_list, name='raptor_list'),
    path('raptor/<int:pk>/', views.raptor_detail, name='raptor_detail'),
    path('raptor/new/', views.raptor_new, name='raptor_new'),
    path('raptor/<int:pk>/edit/', views.raptor_edit, name='raptor_edit'),

    path('songbird/list/', views.songbird_list, name='songbird_list'),
    path('songbird/<int:pk>/', views.songbird_detail, name='songbird_detail'),
    path('songbird/new/', views.songbird_new, name='songbird_new'),
    path('songbird/<int:pk>/edit/', views.songbird_edit, name='songbird_edit'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)