# Generated by Django 4.0.5 on 2022-06-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_orderstatus_parcel_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipment_id',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
