# Generated by Django 2.2.6 on 2019-10-18 09:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20191016_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='addresses',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), size=9), blank=True, null=True, size=None),
        ),
    ]