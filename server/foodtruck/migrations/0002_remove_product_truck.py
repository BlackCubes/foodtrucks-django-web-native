# Generated by Django 3.2.7 on 2021-10-11 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='truck',
        ),
    ]
