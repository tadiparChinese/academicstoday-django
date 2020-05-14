from django.urls import include, path
from . import views

app_name = 'login'

urlpatterns = [
    path('login_modal/', views.login_modal),
    path('login/', views.login_authentication),
    path('logout/', views.logout_authentication),
]
