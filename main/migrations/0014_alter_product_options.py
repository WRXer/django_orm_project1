# Generated by Django 4.2.1 on 2023-06-27 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
