# Generated by Django 3.1.2 on 2020-11-01 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='customers',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='orders',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='pizza',
            new_name='pizzas',
        ),
    ]
