# Generated by Django 4.1 on 2022-08-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_categories_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
