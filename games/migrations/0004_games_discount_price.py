# Generated by Django 3.0.6 on 2020-05-13 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_games_console'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
