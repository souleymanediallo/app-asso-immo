# Generated by Django 3.2.5 on 2021-07-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='size',
            field=models.IntegerField(),
        ),
    ]
