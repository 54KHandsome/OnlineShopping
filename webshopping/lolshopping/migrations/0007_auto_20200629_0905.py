# Generated by Django 3.0.4 on 2020-06-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lolshopping', '0006_account_new_hash_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='new_hash_value',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
