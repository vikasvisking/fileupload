# Generated by Django 2.0 on 2018-04-16 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20180416_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(blank=True, upload_to='documents'),
        ),
    ]
