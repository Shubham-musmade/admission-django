# Generated by Django 2.2.12 on 2021-08-20 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone_num',
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_no',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='text_area',
            field=models.TextField(null=True),
        ),
    ]
