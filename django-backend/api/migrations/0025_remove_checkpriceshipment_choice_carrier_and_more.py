# Generated by Django 4.0.5 on 2022-06-22 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_remove_order_postage_label_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkpriceshipment',
            name='choice_carrier',
        ),
        migrations.RemoveField(
            model_name='checkpriceshipment',
            name='choice_service',
        ),
    ]
