# Generated by Django 2.0.5 on 2018-08-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='check_crop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('temp_start', models.IntegerField()),
                ('temp_end', models.IntegerField()),
                ('pH_start', models.IntegerField()),
                ('pH_end', models.IntegerField()),
                ('info', models.TextField()),
            ],
        ),
    ]
