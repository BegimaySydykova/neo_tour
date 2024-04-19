# Generated by Django 5.0.4 on 2024-04-15 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_alter_tourreview_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourreview',
            name='user_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tourreview',
            name='user_photo',
            field=models.ImageField(null=True, upload_to='user_photos/'),
        ),
    ]
