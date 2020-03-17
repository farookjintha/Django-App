# Generated by Django 3.0.4 on 2020-03-16 11:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('TechnicalCourses', '0004_remove_allcourses_startedfrom'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcourses',
            name='startedfrom',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 11, 51, 49, 614377, tzinfo=utc), verbose_name='Started from'),
            preserve_default=False,
        ),
    ]