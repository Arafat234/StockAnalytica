# Generated by Django 2.2 on 2020-03-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocksearch', '0004_auto_20200306_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystock',
            name='stockname',
            field=models.TextField(blank=True, null=True),
        ),
    ]
