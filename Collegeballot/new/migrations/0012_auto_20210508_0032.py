# Generated by Django 3.2 on 2021-05-07 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0011_alter_data_vc_dept_head_ans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='vc_dept_head_ans',
        ),
        migrations.AddField(
            model_name='data',
            name='s_dept_vc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
