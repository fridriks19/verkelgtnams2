# Generated by Django 3.0.6 on 2020-05-13 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
        ('user', '0004_paymentinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyerinfo',
            name='product',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='games.Games'),
            preserve_default=False,
        ),
    ]