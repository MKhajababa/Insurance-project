# Generated by Django 3.2.5 on 2021-09-28 07:30

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0011_auto_20210928_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None),
        ),
    ]
