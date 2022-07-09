# Generated by Django 4.0.4 on 2022-07-09 21:29

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0002_user_project_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='color',
            field=colorfield.fields.ColorField(choices=[('#50cfbc', '1'), ('#fe7782', '2'), ('#45bfff', '3'), ('#ffbc54', '4'), ('#735bf2', '5')], default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
    ]
