# Generated by Django 4.1.1 on 2022-10-22 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('connector_api', '0002_rename_countries_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nationality',
            field=models.CharField(default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
    ]
