# Generated by Django 4.2.10 on 2024-02-29 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisnessapp', '0003_businessproposal'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessproposal',
            name='Name',
            field=models.CharField(default='default', max_length=30),
        ),
    ]
