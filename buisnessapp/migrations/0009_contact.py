# Generated by Django 5.0 on 2024-03-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisnessapp', '0008_interestedinvestor'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
                ('Message', models.TextField()),
            ],
        ),
    ]