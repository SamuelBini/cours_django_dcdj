# Generated by Django 2.2.5 on 2019-09-26 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ma_bibliotheque', '0003_exemplaire_date_acquisition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exemplaire',
            name='date_acquisition',
            field=models.DateField(auto_now=True),
        ),
    ]
