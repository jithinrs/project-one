# Generated by Django 4.1 on 2022-10-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0043_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Shipped', 'Shipped'), ('Completed', 'Completed'), ('Out for Delivery', 'Out for Delivery'), ('Order cancelled', 'Order cancelled'), ('Returned', 'Returned'), ('Order confirmed', 'Order confirmed')], default='Order confirmed', max_length=150),
        ),
    ]