# Generated by Django 4.1 on 2022-09-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0005_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address_id',
        ),
        migrations.AddField(
            model_name='order',
            name='address_1',
            field=models.CharField(default='a', max_length=1024),
        ),
        migrations.AddField(
            model_name='order',
            name='address_2',
            field=models.CharField(blank=True, default='a', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='a', max_length=256),
        ),
        migrations.AddField(
            model_name='order',
            name='district',
            field=models.CharField(default='a', max_length=256),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='a', max_length=256, verbose_name='you name'),
        ),
        migrations.AddField(
            model_name='order',
            name='pincode',
            field=models.CharField(default='a', max_length=6),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='a', max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Out for shipping', 'Out for shipping'), ('Order Placed', 'Order placed')], default='Pending', max_length=150),
        ),
    ]