# Generated by Django 2.2.6 on 2019-10-26 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0014_company_email01'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email02',
            field=models.EmailField(default='', max_length=254),
        ),
    ]