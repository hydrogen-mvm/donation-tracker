# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-07 04:58


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_remove_event_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmountFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='WordFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=32)),
            ],
        ),
    ]
