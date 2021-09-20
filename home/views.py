from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Register
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .models import Courses
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
import os
import math
import random
import smtplib

from .forms import RegisterForm


def otp():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "home/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="home/password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


# Create your views here.
def home(request):
    return render(request, 'index.html')


@login_required(login_url='/login/')
def admin_home(request):
    obj = Register.objects.get(user=request.user)
    if request.user.is_superuser:
        obj = Register.objects.all()
        return render(request, "admin_home.html", {'objects': obj})
    elif obj.Designation == 'Staff':
        return render(request, "staff_home.html")
    elif obj.Designation == 'Teacher':
        return render(request, "teacher_home.html")
    elif obj.Designation == 'Student':
        return render(request, "student_home.html")


@login_required(login_url='/login/')
def teacher_home(request):
    obj = Register.objects.get(user=request.user)
    if obj.Designation == 'Teacher':
        return render(request, 'teacher_home.html')
    elif obj.Designation == 'Admin':
        return redirect('home:admin_home')
    elif obj.Designation == 'Student':
        return redirect('home:student_home')
    elif obj.Designation == 'Staff':
        return redirect('home:staff_home')


@login_required(login_url='/login/')
def student_home(request):
    obj = Register.objects.get(user=request.user)
    if obj.Designation == 'Student':
        return render(request, 'student_home.html')
    elif obj.Designation == 'Admin':
        return redirect('home:admin_home')
    elif obj.Designation == 'Teacher':
        return redirect('home:teacher_home')
    elif obj.Designation == 'Staff':
        return redirect('home:staff_home')


@login_required(login_url='/login/')
def staff_home(request):
    obj = Register.objects.get(user=request.user)
    if obj.Designation == 'Staff':
        return render(request, 'staff_home.html')
    elif obj.Designation == 'Admin':
        return redirect('home:admin_home')
    elif obj.Designation == 'Teacher':
        return redirect('home:teacher_home')
    elif obj.Designation == 'Student':
        return redirect('home:student_home')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # .get('name')=html value  $$  name=request.== variable
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        gender = request.POST.get('gender')
        qual = request.POST.get('qual')
        mob = request.POST.get('mob')
        desg = request.POST.get('desg')
        username = request.POST.get('username')
        password = request.POST.get('psw')
        email = request.POST.get('email')
        print(name, age, dob, fname, mname, gender, qual, mob, desg)
        try:
            with transaction.atomic():

                if User.objects.filter(username=username).exists():
                    messages.error(request, 'User is already exists')
                    return render(request, 'register.html')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'User is already exists')
                    return render(request, 'register.html')
                else:
                    obj = User.objects.create_user(username=username, password=password, email=email)
                    Register.objects.create(Name=name, Age=age, Dob=dob, FName=fname, MName=mname, Gender=gender,
                                            Qualification=qual, Mob=mob, Designation=desg, Language='', user=obj)
                    # Name,Age...=Database values $$  name,age....== variable

                    messages.success(request, 'Registration Success')  # write code in html also
                    subject = 'welcome to GFG world'
                    message = f'Hi {username}, thank you for registering in geeksforgeeks.'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email, ]
                    send_mail(subject, message, email_from, recipient_list)

                    return render(request, 'login.html')

        except Exception as e:
            print(e)
            messages.error(request, 'Error')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            otp1 = otp()
            # f = open("otpfile.txt", "w")
            # f.write(otp1 + '\n')
            # f.write(username + '\n')
            # f.write(password + '\n')
            # print(otp1)
            subject = 'otp'
            message = f'Hi {user.username}, {otp1}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)

            request.session['username'] = username
            request.session['password'] = password
            request.session['otp'] = otp1

            return render(request, 'otp.html')
        else:
            messages.error(request, 'Invalid UserName or Password')
    else:

        return render(request, 'login.html')


def otp_login(request):
    verify_otp = request.GET.get('otp')
    # f = open("otpfile.txt", "r")
    # print('@@@@@@@@@@@@@@@@@@@@')
    # otp = f.readline()
    # username = f.readline()
    # password = f.readline()
    u = request.session.get('username')
    p = request.session.get('password')
    o = request.session.get('otp')
    print(u, p, o)


    if verify_otp == o:
        user = authenticate(request, username=u, password=p)
        print(user)
        if user is not None:
            login(request,user)
            obj = Register.objects.get(user=request.user)
            if obj.Designation == 'Student':
                return render(request, 'student_home.html')
            elif obj.Designation == 'Admin':
                return redirect('home:admin_home')
            elif obj.Designation == 'Teacher':
                return redirect('home:teacher_home')
            elif obj.Designation == 'Student':
                return redirect('home:student_home')
        else:
            messages.error(request, "User not Exists")
            return redirect('home:login')

    else:
        messages.error(request, "Wrong OTP")
        return redirect('home:login')


def course_details(request, the_slug):  # the_slug code in html also
    print(the_slug)
    if the_slug == 'php':  # 'php'=html value $$ Name=PHP=database value
        obj = Courses.objects.get(Name="PHP")
        return render(request, "course_details.html", {'object': obj})  # Courses = Table name
    elif the_slug == 'java':
        obj = Courses.objects.get(Name="JAVA")
        return render(request, "course_details.html", {'object': obj})
    elif the_slug == 'net':
        obj = Courses.objects.get(Name=".NET")
        return render(request, "course_details.html", {'object': obj})
    else:
        return render(request, 'course_details.html')


def log_out(request):
    logout(request)
    return redirect('home:login')


def details(request, pk):
    obj = Register.objects.get(id=pk)
    messages.success(request, 'Your Details')
    return render(request, "details.html", {'object': obj})


def emp_details(request):
    obj = Register.objects.get(user=request.user)
    if request.user.is_superuser:
        obj = Register.objects.all()
        return render(request, "emp_details.html", {'objects': obj})


def emp_update(request, pk):
    # obj = Register.objects.get(user=request.user)
    if request.method == 'POST':
        name = request.POST.get('name')  # .get('name')=html value  $$  name=request.== variable
        age = request.POST.get('age')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        mob = request.POST.get('mob')
        try:
            Register.objects.filter(id=pk).update(Name=name, Age=age, FName=fname, MName=mname, Mob=mob)
            messages.success(request, 'Updated Successfully')  # write code in html also
            return redirect('home:emp_details')
        except Exception as e:
            print(e)
            messages.error(request, 'Error')
            return render(request, 'emp_details.html')

    else:
        obj = Register.objects.get(id=pk)
        return render(request, "emp_update.html", {'obj': obj})


def emp_delete(request, pk):
    Register.objects.filter(id=pk).delete()
    return redirect('home:emp_details')


def search(request):
    search_tag = request.GET['search']
    obj = Register.objects.filter(Q(Name=search_tag))
    print(obj)
    print(search_tag)
    return render(request, "search.html", {'obj': obj})


def search_details(request, pk):
    obj = Register.objects.get(id=pk)
    return render(request, "search_details.html", {'obj': obj})


def dummy_register(request):
    form = RegisterForm()
    print(form)
    return render(request, 'dummy_register.html', {'form': form})


@login_required(login_url='/login/')
def blog(request):
    return render(request, 'blog.html')


@login_required(login_url='/login/')
def post(request):
    return render(request, 'post.html')


@login_required(login_url='/login/')
def contact(request):
    return render(request, 'contact.html')


@login_required(login_url='/login/')
def subscribe(request):
    subject = 'welcome to GFG world'
    message = f'Hi {request.user.username}, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email, ]
    send_mail(subject, message, email_from, recipient_list)

    return render(request, 'subscribe.html')
