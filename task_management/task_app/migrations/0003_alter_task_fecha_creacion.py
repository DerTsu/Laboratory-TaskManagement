# Generated by Django 5.1.6 on 2025-03-01 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0002_auto_20250301_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
