# Generated by Django 2.2.6 on 2019-10-18 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20191018_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='line1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='line2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='zipCode',
            field=models.CharField(default='', max_length=50),
        ),
    ]