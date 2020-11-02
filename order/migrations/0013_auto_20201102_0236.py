# Generated by Django 3.1.2 on 2020-11-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20201102_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(choices=[('cancelled', 'cancelled'), ('delivering', 'delivering'), ('delivered', 'delivered'), ('pending', 'no_checkout'), ('preparing', 'preparing'), ('ready', 'ready')], default='pending', max_length=10),
        ),
    ]
