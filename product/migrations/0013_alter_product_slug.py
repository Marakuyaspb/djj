# Generated by Django 4.1.12 on 2023-11-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_productimage_caption_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]