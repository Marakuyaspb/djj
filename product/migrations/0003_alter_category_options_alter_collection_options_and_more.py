# Generated by Django 4.2.2 on 2023-10-23 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_options_alter_collection_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['collection'], 'verbose_name': 'Коллекция', 'verbose_name_plural': 'Коллекции'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
