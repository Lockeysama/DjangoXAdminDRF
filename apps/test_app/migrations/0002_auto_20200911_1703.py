# Generated by Django 2.2.2 on 2020-09-11 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='age',
            field=models.IntegerField(
                blank=True, help_text='年龄', null=True, verbose_name='年龄'
            ),
        ),
    ]