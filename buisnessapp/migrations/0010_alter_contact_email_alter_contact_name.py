# Generated by Django 4.2.4 on 2024-03-25 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisnessapp', '0009_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Name',
            field=models.CharField(max_length=30),
        ),
    ]