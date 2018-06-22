# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-22 01:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_registration', '0002_user_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='login_registration.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='posted_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='the_wall.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='sender_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='login_registration.User'),
        ),
    ]
