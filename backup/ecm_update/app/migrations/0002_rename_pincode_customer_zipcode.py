# Generated by Django 4.1 on 2022-08-12 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='pincode',
            new_name='zipcode',
        ),
    ]
