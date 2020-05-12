# Generated by Django 3.0.6 on 2020-05-12 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=999)),
                ('price', models.FloatField()),
                ('on_sale', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ComputersImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=999)),
                ('computers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computers.Computers')),
            ],
        ),
    ]
