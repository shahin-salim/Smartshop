# Generated by Django 3.2 on 2022-02-09 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0023_products_processor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='processor',
            field=models.CharField(choices=[('Snapdragon', 'Snapdragon'), ('MediaTek', 'MediaTek'), ('bionic', 'bionic')], max_length=20),
        ),
    ]