# Generated by Django 3.1.2 on 2020-11-02 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20201101_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='checkout_time',
        ),
        migrations.AddField(
            model_name='order',
            name='checkout_status',
            field=models.BooleanField(default=False),
        ),
    ]
