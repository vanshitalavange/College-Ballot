# Generated by Django 3.2 on 2021-04-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_data_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='pcr',
            field=models.CharField(default='', max_length=10),
        ),
    ]
