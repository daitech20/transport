# Generated by Django 4.0.5 on 2022-06-09 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_order_status_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_detail',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order_detail',
            name='shipment_id',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Order_Detail',
        ),
        migrations.DeleteModel(
            name='Order_Status',
        ),
        migrations.DeleteModel(
            name='Shipment',
        ),
    ]
