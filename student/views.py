from django.shortcuts import render, HttpResponse


def registration(request):
    return render(request, 'register.html')


def updation(request):
    return HttpResponse('ITS AN UPDATION PAGE')


def login(request):
    return HttpResponse('LOGIN PAGE OF A STUDENT')


def home(request):
    return render(request, 'blog.html')

# Create your views here.
