# Generated by Django 4.1.12 on 2023-12-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_popoverfeatures_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fabriciconchange',
            options={'ordering': ['product_fabric_name'], 'verbose_name': 'Иконка переключения ткани', 'verbose_name_plural': 'Иконки переключения ткани'},
        ),
        migrations.RemoveIndex(
            model_name='fabriciconchange',
            name='product_fab_product_ca6b7e_idx',
        ),
        migrations.RenameField(
            model_name='fabriciconchange',
            old_name='product_fabric_icon_name',
            new_name='product_fabric_name',
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Сокращенно латиницей (arm, str, k1r и т.п.)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_ru',
            field=models.CharField(max_length=50, verbose_name='Название категории (по-русски, в множественом числе)'),
        ),
        migrations.AddIndex(
            model_name='fabriciconchange',
            index=models.Index(fields=['product_fabric_name'], name='product_fab_product_74676f_idx'),
        ),
    ]