# Generated by Django 3.2 on 2022-01-26 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0020_auto_20220126_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.AddField(
            model_name='order',
            name='address_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userApp.address'),
        ),
    ]