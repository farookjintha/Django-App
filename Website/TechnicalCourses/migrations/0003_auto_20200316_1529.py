# Generated by Django 3.0.4 on 2020-03-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechnicalCourses', '0002_auto_20200316_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allcourses',
            name='startedfrom',
            field=models.DateTimeField(verbose_name='Started from'),
        ),
    ]
