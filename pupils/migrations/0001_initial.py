# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-21 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('published', models.DateTimeField(verbose_name='Publish date')),
                ('image', models.FileField(upload_to='images/')),
                ('age', models.DateField(verbose_name='Date of Birth')),
                ('breed', models.TextField(verbose_name='Breed')),
            ],
        ),
    ]
