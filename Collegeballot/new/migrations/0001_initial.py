# Generated by Django 3.2 on 2021-04-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('year', models.CharField(max_length=45)),
                ('dept', models.CharField(max_length=45)),
                ('div', models.CharField(max_length=45)),
                ('rollno', models.CharField(max_length=45)),
                ('login_id', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),

            ],
        ),
    ]
