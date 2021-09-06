from django.urls import path
from api import views

urlpatterns = [
    path('register_list/', views.register_list),
    path('register_detail/<int:pk>/', views.register_detail),
    path('api/<int:pk>/', views.register_list),
]
