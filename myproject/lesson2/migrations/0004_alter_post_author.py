# Generated by Django 4.2.3 on 2023-08-01 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson2', '0003_user_new_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='lesson2.author'),
        ),
    ]
