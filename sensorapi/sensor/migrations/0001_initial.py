# Generated by Django 2.2.6 on 2019-10-08 14:06

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_name', models.CharField(max_length=70)),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=14)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=14)),
                ('easting', models.DecimalField(decimal_places=4, max_digits=14)),
                ('northing', models.DecimalField(decimal_places=4, max_digits=14)),
                ('elevation', models.DecimalField(decimal_places=4, max_digits=10)),
                ('install_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='SensorReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading_date', models.DateTimeField()),
                ('reading', models.DecimalField(decimal_places=4, max_digits=14)),
                ('sensor_name', models.ForeignKey(db_column='sensor_name', on_delete=django.db.models.deletion.CASCADE, to='sensor.SensorDetail')),
            ],
        ),
    ]
