# Generated by Django 4.0.4 on 2022-09-17 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='get',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
