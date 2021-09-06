from django.db import models


# Create your models here.
class Dummy(models.Model):
    Name = models.CharField(max_length=25, blank=True, null=True)
    Age = models.CharField(max_length=30, blank=True, null=True)
    FName = models.CharField(max_length=25, blank=True, null=True)
