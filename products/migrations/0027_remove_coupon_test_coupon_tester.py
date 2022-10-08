# Generated by Django 4.1 on 2022-10-03 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_coupon_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='test',
        ),
        migrations.AddField(
            model_name='coupon',
            name='tester',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]