# Generated by Django 3.1 on 2020-08-30 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20200830_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
