from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration),
    path('updation/', views.updation),
    path('login/', views.login),
    path('home/', views.home),
]