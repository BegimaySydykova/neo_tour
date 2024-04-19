# Generated by Django 5.0.4 on 2024-04-11 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_people', models.IntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('additional_comments', models.TextField(blank=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tour')),
            ],
        ),
    ]
