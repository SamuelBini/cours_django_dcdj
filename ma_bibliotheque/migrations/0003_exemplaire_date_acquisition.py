# Generated by Django 2.2.5 on 2019-09-26 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ma_bibliotheque', '0002_auto_20190926_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='exemplaire',
            name='date_acquisition',
            field=models.DateField(auto_now_add=True, default='2019-09-06'),
            preserve_default=False,
        ),
    ]
