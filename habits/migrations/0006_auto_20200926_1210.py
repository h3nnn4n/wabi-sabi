# Generated by Django 3.1.1 on 2020-09-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_auto_20200926_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]
