# Generated by Django 4.1.12 on 2023-12-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_slug',
            field=models.SlugField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]