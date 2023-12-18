# Generated by Django 5.0 on 2023-12-15 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_product_product_fabric_icon_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='popoverfeatures',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='features', to='product.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='popoverfeatures',
            name='collection',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='features', to='product.collection', verbose_name='Коллекция'),
        ),
        migrations.AlterField(
            model_name='popoverfeatures',
            name='popover_name',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Название набора 5 фич'),
        ),
        migrations.AlterField(
            model_name='product',
            name='carousel_items',
            field=models.ManyToManyField(blank=True, related_name='carousel_items', to='product.productimage', verbose_name='Слайдер с товаром | десктоп'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]