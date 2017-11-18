# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arendator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=30, verbose_name='ФИО')),
                ('gos_num', models.CharField(max_length=9, verbose_name='Гос. номер')),
                ('box_num', models.CharField(max_length=3, unique=True, verbose_name='Номер бокса')),
                ('auto', models.CharField(choices=[('N', 'Nissan'), ('M', 'Mitsubisi'), ('L', 'Lada')], max_length=1, verbose_name='Марка машины')),
                ('has_pass', models.BooleanField(default=False, verbose_name='Пропуск получен')),
                ('registered', models.DateField(default=django.utils.timezone.now)),
                ('ended', models.DateField(blank=True, null=True)),
            ],
        ),
    ]