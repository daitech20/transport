# Generated by Django 4.0.5 on 2022-06-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_shipment_from_phone_alter_shipment_from_zip_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
