# Generated by Django 3.2.6 on 2021-09-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dummy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=25, null=True)),
                ('Age', models.CharField(blank=True, max_length=30, null=True)),
                ('FName', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]