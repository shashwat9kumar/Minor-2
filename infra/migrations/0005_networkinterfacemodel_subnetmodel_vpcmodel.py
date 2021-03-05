# Generated by Django 3.1.6 on 2021-02-24 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0004_auto_20210216_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkInterfaceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('privateips', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubnetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('vpcid', models.CharField(max_length=100)),
                ('cidrblock', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VPCModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('cidrblock', models.CharField(max_length=100)),
            ],
        ),
    ]
