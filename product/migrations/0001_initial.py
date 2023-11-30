# Generated by Django 4.1.12 on 2023-11-28 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
                ('category_ru', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_id', models.AutoField(primary_key=True, serialize=False)),
                ('collection', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
                'ordering': ['collection'],
            },
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('fabric_id', models.AutoField(primary_key=True, serialize=False)),
                ('fabric_name', models.CharField(max_length=50)),
                ('product_fabric_img', models.ImageField(upload_to='fabric_images/')),
                ('product_fabric_about', models.CharField(max_length=1500)),
            ],
            options={
                'verbose_name': 'Ткань',
                'verbose_name_plural': 'Ткани',
                'ordering': ['fabric_name'],
            },
        ),
        migrations.CreateModel(
            name='FabricIconChange',
            fields=[
                ('fabric_icon_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_fabric_icon', models.ImageField(upload_to='fabric_images/')),
            ],
            options={
                'verbose_name': 'Иконка переключения ткани',
                'verbose_name_plural': 'Иконки переключения ткани',
                'ordering': ['product_fabric_icon'],
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('option_id', models.AutoField(primary_key=True, serialize=False)),
                ('option_name', models.CharField(blank=True, max_length=350, null=True)),
                ('option_1_img', models.ImageField(upload_to='options/')),
                ('option_1_description', models.CharField(max_length=500)),
                ('option_2_img', models.ImageField(upload_to='options/')),
                ('option_2_description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Опция',
                'verbose_name_plural': 'Опции',
                'ordering': ['option_name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('product_type', models.CharField(blank=True, max_length=50, null=True)),
                ('product_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('popular', models.BooleanField(default=True)),
                ('is_new', models.BooleanField(default=True)),
                ('available_for_delivery_2', models.BooleanField(default=True)),
                ('available_for_delivery_28', models.BooleanField(default=True)),
                ('available_in_showroom', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=1500, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_sale', models.DecimalField(decimal_places=2, max_digits=10)),
                ('closeup', models.ImageField(blank=True, null=True, upload_to='closeups/')),
                ('width', models.IntegerField(blank=True, null=True)),
                ('depth', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('pdf', models.CharField(blank=True, max_length=150, null=True)),
                ('product_inside', models.CharField(blank=True, max_length=150, null=True)),
                ('product_inside_pillow', models.CharField(blank=True, max_length=150, null=True)),
                ('carcas_type', models.CharField(blank=True, max_length=50, null=True)),
                ('paws_type', models.CharField(blank=True, max_length=50, null=True)),
                ('mechanism_type', models.CharField(blank=True, max_length=50, null=True)),
                ('sleep_place', models.CharField(blank=True, max_length=50, null=True)),
                ('linen_drawer', models.CharField(blank=True, max_length=50, null=True)),
                ('scheme', models.CharField(blank=True, max_length=150, null=True)),
                ('features', models.CharField(blank=True, max_length=350, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(default='', max_length=350)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['product_full_name'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.option')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='carousel_items',
            field=models.ManyToManyField(blank=True, related_name='carousel_items', to='product.productimage'),
        ),
        migrations.AddField(
            model_name='product',
            name='carousel_items_mob',
            field=models.ManyToManyField(blank=True, related_name='carousel_items_mob', to='product.productimage'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.collection'),
        ),
        migrations.AddField(
            model_name='product',
            name='fabric_name',
            field=models.ForeignKey(db_column='products', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.fabric'),
        ),
        migrations.AddField(
            model_name='product',
            name='options',
            field=models.ManyToManyField(blank=True, to='product.option'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_fabric_icon',
            field=models.ManyToManyField(blank=True, to='product.fabriciconchange'),
        ),
        migrations.AddField(
            model_name='product',
            name='slider_interior',
            field=models.ManyToManyField(blank=True, related_name='slider_interior', to='product.productimage'),
        ),
        migrations.AddField(
            model_name='product',
            name='slider_interior_mob',
            field=models.ManyToManyField(blank=True, related_name='slider_interior_mob', to='product.productimage'),
        ),
        migrations.AddIndex(
            model_name='option',
            index=models.Index(fields=['option_name'], name='product_opt_option__ae3011_idx'),
        ),
        migrations.AddIndex(
            model_name='fabriciconchange',
            index=models.Index(fields=['product_fabric_icon'], name='product_fab_product_ca6b7e_idx'),
        ),
        migrations.AddIndex(
            model_name='fabric',
            index=models.Index(fields=['fabric_name'], name='product_fab_fabric__f5fc2a_idx'),
        ),
        migrations.AddIndex(
            model_name='collection',
            index=models.Index(fields=['collection'], name='product_col_collect_386316_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['category'], name='product_cat_categor_a164b2_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['id', 'slug', '-created'], name='product_pro_id_7c37c2_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['product_full_name'], name='product_pro_product_63afbd_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-created'], name='product_pro_created_942044_idx'),
        ),
    ]
