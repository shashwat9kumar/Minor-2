# Generated by Django 3.1.5 on 2021-02-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0002_keymodel_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstanceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ami', models.CharField(max_length=100)),
                ('instancetype', models.CharField(max_length=100)),
            ],
        ),
    ]
