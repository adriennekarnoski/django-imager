# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 21:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('website', models.URLField()),
                ('location', models.CharField(max_length=30)),
                ('fee', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('camera', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('CANON', 'Canon'), ('NIKON', 'Nikon'), ('SONY', 'Sony'), ('FUJIFILM', 'Fujifilm')], max_length=25)),
                ('services', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('WEDDINGS', 'Weddings'), ('SCHOOL', 'School'), ('FAMILY', 'Family'), ('BABIES', 'Babies'), ('NATURE', 'Nature'), ('ABSTACT', 'Abstract'), ('OTHER', 'Other')], max_length=50)),
                ('bio', models.TextField(blank=True)),
                ('photo_styles', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('BW', 'Black and white'), ('COLOR', 'Color'), ('STILL', 'Still'), ('ACTION', 'Action')], max_length=21)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
