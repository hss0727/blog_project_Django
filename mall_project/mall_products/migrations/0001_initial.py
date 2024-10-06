# Generated by Django 5.1 on 2024-08-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MallProductClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=256, verbose_name='Product Name')),
                ('product_price', models.IntegerField(verbose_name='Product Price')),
                ('product_description', models.TextField(verbose_name='Product Description')),
                ('product_stock', models.IntegerField(verbose_name='Product Stock')),
                ('product_reg_dttm', models.DateTimeField(auto_now_add=True, verbose_name='Registered Date Time of the Product')),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
                'db_table': 'mall_product_db',
            },
        ),
    ]
