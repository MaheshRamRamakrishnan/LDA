# Generated by Django 4.0.7 on 2022-09-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualitycontrol', '0002_raw_materials'),
    ]

    operations = [
        migrations.CreateModel(
            name='quality_team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('employee_id', models.CharField(max_length=200, null=True)),
                ('Supplier', models.CharField(max_length=200, null=True)),
                ('inspection_team_type', models.CharField(max_length=200, null=True)),
                ('raw_material_quality', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]