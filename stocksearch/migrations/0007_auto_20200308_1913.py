# Generated by Django 2.2 on 2020-03-08 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocksearch', '0006_auto_20200306_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='mystock',
            name='changepct',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mystock',
            name='close',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mystock',
            name='high',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mystock',
            name='low',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mystock',
            name='open',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mystock',
            name='volume',
            field=models.TextField(blank=True, null=True),
        ),
    ]
