# Generated by Django 3.2.10 on 2022-01-31 21:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0010_user_profile7979'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 21, 51, 8, 685994, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
