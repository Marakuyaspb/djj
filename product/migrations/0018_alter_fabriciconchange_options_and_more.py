# Generated by Django 4.1.12 on 2023-12-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_fabriciconchange_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fabriciconchange',
            options={'ordering': ['fabric_name'], 'verbose_name': 'Иконка переключения ткани', 'verbose_name_plural': 'Иконки переключения ткани'},
        ),
        migrations.RemoveIndex(
            model_name='fabriciconchange',
            name='product_fab_product_74676f_idx',
        ),
        migrations.RenameField(
            model_name='fabriciconchange',
            old_name='product_fabric_name',
            new_name='fabric_name',
        ),
        migrations.AddIndex(
            model_name='fabriciconchange',
            index=models.Index(fields=['fabric_name'], name='product_fab_fabric__34f8d6_idx'),
        ),
    ]