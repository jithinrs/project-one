# Generated by Django 4.1 on 2022-10-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_remove_coupon_tester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateField(),
        ),
    ]
