# Generated by Django 3.1.7 on 2021-02-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=200),
        ),
    ]
