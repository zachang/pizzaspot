# Generated by Django 3.1.2 on 2020-11-01 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20201101_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='08099999999', max_length=14),
            preserve_default=False,
        ),
    ]
