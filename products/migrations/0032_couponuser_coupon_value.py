# Generated by Django 4.1 on 2022-10-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_couponuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponuser',
            name='coupon_value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
