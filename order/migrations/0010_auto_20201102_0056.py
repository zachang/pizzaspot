# Generated by Django 3.1.2 on 2020-11-02 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20201102_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(choices=[('cancelled', 'cancelled'), ('delivering', 'delivering'), ('delivered', 'delivered'), (None, 'no checkout'), ('preparing', 'preparing'), ('ready', 'ready')], default=None, max_length=10),
        ),
    ]
