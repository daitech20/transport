# Generated by Django 4.0.5 on 2022-06-05 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_order_order_status_shipment_order_detail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='from_phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='from_zip',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='to_phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='to_zip',
            field=models.IntegerField(),
        ),
    ]