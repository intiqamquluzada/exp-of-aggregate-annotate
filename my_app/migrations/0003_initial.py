# Generated by Django 4.2.6 on 2023-10-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_app', '0002_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of product')),
                ('price', models.FloatField(verbose_name='Price of product')),
                ('count', models.IntegerField(verbose_name='Count of product')),
                ('color', models.CharField(max_length=255, verbose_name='Color of product')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('name',),
            },
        ),
    ]
