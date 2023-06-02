# Generated by Django 4.2.1 on 2023-05-30 15:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_created_for_hk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='blog_name')),
                ('slug', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True, verbose_name='blog_description')),
                ('image', models.ImageField(upload_to='images')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
                ('blog_views', models.IntegerField(default=0, verbose_name='blog_views')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_for_hk',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
