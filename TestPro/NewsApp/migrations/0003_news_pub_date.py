# Generated by Django 3.1.5 on 2021-02-03 09:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0002_sportnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 2, 3, 9, 48, 33, 525987, tzinfo=utc)),
        ),
    ]