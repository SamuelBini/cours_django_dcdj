# Generated by Django 2.2.5 on 2019-09-26 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ma_bibliotheque', '0005_remove_exemplaire_date_acquisition'),
    ]

    operations = [
        migrations.AddField(
            model_name='exemplaire',
            name='date_acquisition',
            field=models.DateField(auto_now_add=True, default='2019-09-06'),
            preserve_default=False,
        ),
    ]