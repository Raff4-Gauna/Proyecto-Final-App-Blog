# Generated by Django 3.2.6 on 2023-07-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20230729_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.CharField(choices=[('unverified', 'unverified'), ('verified', 'verified')], default='unverified', max_length=10),
        ),
    ]
