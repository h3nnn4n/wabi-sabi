# Generated by Django 3.1.1 on 2020-09-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0009_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
