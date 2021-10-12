# Generated by Django 3.2.7 on 2021-10-11 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_alter_like_product'),
        ('foodtruck', '0002_remove_product_truck'),
        ('review', '0003_alter_review_product'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Product',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name='Product',
                    table='product_product',
                ),
            ],
        ),
    ]