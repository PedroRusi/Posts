# Generated by Django 4.1.4 on 2022-12-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publicate',
            field=models.BooleanField(default=False),
        ),
    ]