# Generated by Django 4.0.1 on 2022-01-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='date_filmed',
            field=models.DateField(null=True),
        ),
    ]
