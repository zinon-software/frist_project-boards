# Generated by Django 3.1.7 on 2021-03-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bor', '0003_auto_20210228_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]
