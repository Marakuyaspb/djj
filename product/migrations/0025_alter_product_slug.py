# Generated by Django 4.1.12 on 2023-12-01 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_remove_product_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]