# Generated by Django 4.1.12 on 2023-12-01 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_remove_product_product_fabric_about_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popoverfeatures',
            name='collection',
        ),
    ]