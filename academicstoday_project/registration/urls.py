#from django.conf.urls import patterns, include, url
from django.urls import path, include
from . import views

app_name = 'registration'

urlpatterns = [
    path('register_modal/', views.register_modal),
    path('register/', views.register),

]
