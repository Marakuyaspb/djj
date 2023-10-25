# Generated by Django 4.2.2 on 2023-10-23 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['collection'], 'verbose_name': 'collection', 'verbose_name_plural': 'collections'},
        ),
        migrations.RemoveIndex(
            model_name='category',
            name='product_cat_name_4f76a1_idx',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='collection',
            old_name='name',
            new_name='collection',
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['category'], name='product_cat_categor_a164b2_idx'),
        ),
        migrations.AddIndex(
            model_name='collection',
            index=models.Index(fields=['collection'], name='product_col_collect_386316_idx'),
        ),
    ]
