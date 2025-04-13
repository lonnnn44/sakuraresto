from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('team/', views.team, name='team'),
    path('about/', views.about, name='about'),
    path('special-dishes/', views.special_dishes, name='special-dishes'),
]