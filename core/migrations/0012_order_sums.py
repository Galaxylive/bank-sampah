# Generated by Django 2.2.5 on 2019-10-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20191019_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sums',
            field=models.BooleanField(default=True),
        ),
    ]