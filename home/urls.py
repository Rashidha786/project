from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.log_in, name='login'),
    path('otp_login/', views.otp_login, name='otp_login'),
    path('otp/', views.otp, name='otp'),
    path('register/details/<int:pk>/', views.details, name='details'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_home/emp_details/', views.emp_details, name='emp_details'),
    path('admin_home/emp_update/<int:pk>/', views.emp_update, name='emp_update'),
    path('admin_home/emp_delete/<int:pk>/', views.emp_delete, name='emp_delete'),
    path('admin_home/search/', views.search, name='search'),
    path('admin_home/search_details/<int:pk>/', views.search_details, name='search_details'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('post/', views.post, name='post'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('teacher_home/', views.teacher_home, name='teacher_home'),
    path('student_home/', views.student_home, name='student_home'),
    path('student_home/<slug:the_slug>/', views.course_details, name='course_details'),
    path('staff_home/', views.staff_home, name='staff_home'),
    path('logout', views.log_out, name='log_out'),

    path('form_register/', views.dummy_register, name='form_register'),

    path("password_reset", views.password_reset_request, name="password_reset")
]
