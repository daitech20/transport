# Generated by Django 4.0.5 on 2022-06-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_remove_order_rate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True),
        ),
    ]