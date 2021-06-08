from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('allsongs/', views.allsongs),
    path('allsongs/<int:id>', views.songpost),
    path('search', views.search, name= 'search'),
]