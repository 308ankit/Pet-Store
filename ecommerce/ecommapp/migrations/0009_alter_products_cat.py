# Generated by Django 4.2.5 on 2023-11-01 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0008_order_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Collars,Leashes&Harnesses'), (2, 'Food'), (3, 'Cloth'), (4, 'Toys'), (5, 'Health&Hygienes'), (6, 'Bowls&Feeders'), (7, 'Pharmacy')], verbose_name='Category'),
        ),
    ]
