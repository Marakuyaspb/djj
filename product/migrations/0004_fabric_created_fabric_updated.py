# Generated by Django 4.1.12 on 2023-11-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_option_created_option_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabric',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fabric',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]