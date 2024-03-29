# Generated by Django 4.1.3 on 2023-05-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mca', '0010_profile_dob_profile_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100, verbose_name='Event name')),
                ('event_date', models.DateField(verbose_name='Date')),
                ('event_location', models.CharField(max_length=100, verbose_name='Location')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, default='2001-08-08'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='workplace',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
