# Generated by Django 3.1.5 on 2021-02-16 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0003_instancemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instancemodel',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
