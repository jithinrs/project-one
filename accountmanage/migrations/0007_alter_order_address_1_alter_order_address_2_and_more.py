# Generated by Django 4.1 on 2022-09-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0006_remove_order_address_id_order_address_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_1',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_2',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='district',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=256, verbose_name='you name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for shipping', 'Out for shipping'), ('Order Placed', 'Order placed'), ('Completed', 'Completed')], default='Pending', max_length=150),
        ),
    ]
