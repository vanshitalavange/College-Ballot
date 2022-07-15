# Generated by Django 3.2 on 2021-04-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0006_pcr_pcr_votecount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='pcr',
        ),
        migrations.AddField(
            model_name='data',
            name='ans',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='data',
            name='ans1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='data',
            name='ans2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='data',
            name='cr_vc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='data',
            name='crformfilled',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='data',
            name='elected_cr',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='data',
            name='elected_dept_head',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='data',
            name='final_dept',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='data',
            name='hod',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='data',
            name='president',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='data',
            name='vc_dept_head_ans',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='data',
            name='vc_pcr',
            field=models.IntegerField(default=0),
        ),
    ]
