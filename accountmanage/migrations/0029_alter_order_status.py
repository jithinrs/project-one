# Generated by Django 4.1 on 2022-09-30 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0028_alter_order_status_userpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order cancelled', 'Order cancelled'), ('Shipped', 'Shipped'), ('Returned', 'Returned'), ('Out for Delivery', 'Out for Delivery'), ('Order confirmed', 'Order confirmed'), ('Completed', 'Completed')], default='Order confirmed', max_length=150),
        ),
    ]
