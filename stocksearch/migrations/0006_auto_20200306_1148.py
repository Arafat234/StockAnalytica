# Generated by Django 2.2 on 2020-03-06 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocksearch', '0005_auto_20200306_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystock',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
