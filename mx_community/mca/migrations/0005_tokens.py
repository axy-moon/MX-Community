# Generated by Django 4.1.3 on 2022-12-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mca', '0004_post_title_alter_post_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='tokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=7, unique=True, verbose_name='Roll No')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
            ],
        ),
    ]
