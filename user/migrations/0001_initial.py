# Generated by Django 4.2.5 on 2024-04-25 08:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_full_name', message='Invalid full name', regex='^[а-яА-ЯёЁa-zA-Z]+\\s[а-яА-ЯёЁa-zA-Z]+\\s[а-яА-ЯёЁa-zA-Z]+$')])),
                ('password', models.CharField(max_length=250, validators=[django.core.validators.RegexValidator(code='invalid_password', message='Invalid password', regex='^[A-Za-z\\d!@#$%^&*()_+]+$')])),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(regex='^1?\\d{9,15}$')])),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
