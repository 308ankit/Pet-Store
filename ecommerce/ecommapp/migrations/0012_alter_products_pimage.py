# Generated by Django 4.2.5 on 2023-11-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0011_alter_products_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pimage',
            field=models.ImageField(upload_to='user_images'),
        ),
    ]
