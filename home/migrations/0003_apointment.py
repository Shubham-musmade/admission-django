# Generated by Django 2.2.12 on 2021-08-26 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210820_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=50)),
                ('a_email', models.CharField(max_length=100)),
                ('a_phone_no', models.CharField(max_length=12, null=True)),
                ('a_text_area', models.TextField(null=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
