# Generated by Django 2.2.7 on 2019-12-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inetapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcre',
            name='website',
            field=models.CharField(max_length=50),
        ),
    ]
