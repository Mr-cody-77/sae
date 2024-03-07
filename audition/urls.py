from django.contrib import admin
from django.urls import path, include
from audition import views

urlpatterns = [
    path('', views.home,name='home'),
    path('audition', views.form,name='form'),
]