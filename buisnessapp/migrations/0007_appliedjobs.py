# Generated by Django 4.2.10 on 2024-02-29 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisnessapp', '0006_alter_query_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='appliedjobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BusinessMan', models.CharField(max_length=30)),
                ('Business', models.CharField(max_length=30)),
                ('Applicant', models.CharField(max_length=30)),
                ('NoticePeriod', models.CharField(max_length=30)),
                ('ExpectedSalary', models.IntegerField()),
                ('Status', models.CharField(choices=[('pending', 'Pending'), ('you can attend interview', 'Accepted'), ('Rejected', 'Declined')], default='pending your application', max_length=30)),
            ],
        ),
    ]
