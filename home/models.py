from django.db import models
from django.contrib.auth.models import User


class Login(models.Model):
    username = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=25, blank=True, null=True)


class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=25, blank=True, null=True)
    Age = models.CharField(max_length=30, blank=True, null=True)
    Dob = models.CharField(max_length=30, blank=True, null=True)
    FName = models.CharField(max_length=25, blank=True, null=True)
    MName = models.CharField(max_length=25, blank=True, null=True)
    Gender = models.CharField(max_length=25, blank=True, null=True)
    Qualification = models.CharField(max_length=30, blank=True, null=True)
    Language = models.CharField(max_length=25, blank=True, null=True)
    Mob = models.CharField(max_length=30, blank=True, null=True)
    Designation = models.CharField(max_length=25, blank=True, null=True)

class Courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=34, blank=True, null=True)
    Qualification = models.CharField(max_length=23, blank=True, null=True)
    Duration = models.CharField(max_length=25, blank=True, null=True)
    Fee = models.CharField(max_length=25, blank=True, null=True)

