# Generated by Django 3.2.6 on 2021-08-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='FName',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='Gender',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='Language',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='MName',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='Mob',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='Name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='Qualification',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
