# Generated by Django 5.0 on 2023-12-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_productimage_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='icon_available_for_delivery_2',
            field=models.ImageField(blank=True, null=True, upload_to='status_icons/%Y/%m/%d', verbose_name='Иконка | Доставим за 2 дня'),
        ),
        migrations.AddField(
            model_name='product',
            name='icon_available_for_delivery_28',
            field=models.ImageField(blank=True, null=True, upload_to='status_icons/%Y/%m/%d', verbose_name='Иконка | Доставим за 28 дней'),
        ),
        migrations.AddField(
            model_name='product',
            name='icon_available_in_showroom',
            field=models.ImageField(blank=True, null=True, upload_to='status_icons/%Y/%m/%d', verbose_name='Иконка | Есть в шоуруме'),
        ),
        migrations.AddField(
            model_name='product',
            name='icon_is_new',
            field=models.ImageField(blank=True, null=True, upload_to='status_icons/%Y/%m/%d', verbose_name='Иконка | Новый'),
        ),
    ]
