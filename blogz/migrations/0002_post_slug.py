# Generated by Django 2.2.4 on 2019-08-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1, max_length=250, unique_for_date='publish'),
            preserve_default=False,
        ),
    ]
