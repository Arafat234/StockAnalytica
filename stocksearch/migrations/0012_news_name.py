# Generated by Django 2.2 on 2020-03-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocksearch', '0011_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
