# Generated by Django 3.0.6 on 2020-05-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computers',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]