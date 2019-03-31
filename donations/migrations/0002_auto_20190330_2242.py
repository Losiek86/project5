# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-30 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonateOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank='False', max_length=50)),
                ('phone_number', models.CharField(blank='False', max_length=20)),
                ('country', models.CharField(blank='False', max_length=40)),
                ('postcode', models.CharField(blank='False', max_length=20)),
                ('town_or_city', models.CharField(blank='False', max_length=40)),
                ('street_address1', models.CharField(blank='False', max_length=40)),
                ('street_address2', models.CharField(blank='False', max_length=40)),
                ('county', models.CharField(blank='False', max_length=40)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DonateOrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='donate',
            name='image',
            field=models.ImageField(upload_to='donations/'),
        ),
        migrations.AddField(
            model_name='donateorderlineitem',
            name='donate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.Donate'),
        ),
        migrations.AddField(
            model_name='donateorderlineitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.DonateOrder'),
        ),
    ]
