# Generated by Django 4.2.1 on 2023-05-11 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
