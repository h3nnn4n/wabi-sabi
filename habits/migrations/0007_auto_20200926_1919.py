# Generated by Django 3.1.1 on 2020-09-26 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_auto_20200926_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
