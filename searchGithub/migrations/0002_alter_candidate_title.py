# Generated by Django 4.1.1 on 2022-09-24 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchGithub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]
