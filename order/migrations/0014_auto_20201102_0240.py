# Generated by Django 3.1.2 on 2020-11-02 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20201102_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(choices=[('cancelled', 'cancelled'), ('delivering', 'delivering'), ('delivered', 'delivered'), ('pending', 'pending'), ('preparing', 'preparing'), ('ready', 'ready')], default='pending', max_length=10),
        ),
    ]
