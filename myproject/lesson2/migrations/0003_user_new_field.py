# Generated by Django 4.2.3 on 2023-07-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson2', '0002_author_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='new_field',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
