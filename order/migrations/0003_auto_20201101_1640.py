# Generated by Django 3.1.2 on 2020-11-01 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20201101_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customers',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='orders',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='pizzas',
            new_name='pizza',
        ),
    ]
