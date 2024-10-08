# Generated by Django 5.0.7 on 2024-08-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.SlugField(default='', verbose_name='اسلاگ')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'لیست دسته بندی ها',
            },
        ),
    ]
