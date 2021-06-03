# Generated by Django 3.1.12 on 2021-06-03 07:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worktrip', '0003_auto_20210603_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_speed', models.IntegerField(default=0)),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(default='', max_length=100)),
                ('upload_speed', models.IntegerField(default=0)),
                ('venue_type', models.CharField(default='', max_length=100)),
                ('venue_url', models.CharField(default='', max_length=255)),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]