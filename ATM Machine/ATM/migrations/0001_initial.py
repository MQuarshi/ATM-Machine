# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-21 01:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 10', regex='^.{10}$')])),
                ('phonenum', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 7', regex='^.{7}$')])),
                ('name', models.TextField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account_type', models.CharField(choices=[('SAVINGS', 'Savings'), ('CHECKING', 'Checking')], default='CHECKING', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='ATM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ATM.User'),
        ),
    ]