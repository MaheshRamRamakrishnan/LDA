# Generated by Django 4.0.7 on 2022-09-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0005_manufacturing_process_final'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturing_process',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
