# Generated by Django 4.1.12 on 2023-11-07 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_product_fabric_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='fabric_type',
        ),
    ]
