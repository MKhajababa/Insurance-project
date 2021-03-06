# Generated by Django 3.2.5 on 2021-09-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0003_feedback_leaddetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='agentuser',
            name='pic',
            field=models.ImageField(blank=True, default=3, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
