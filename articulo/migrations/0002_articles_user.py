# Generated by Django 3.2.6 on 2023-07-28 01:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
