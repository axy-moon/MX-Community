# Generated by Django 4.1.3 on 2023-05-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mca', '0012_post_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Others', max_length=40),
        ),
    ]
