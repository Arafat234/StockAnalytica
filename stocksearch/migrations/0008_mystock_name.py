# Generated by Django 2.2 on 2020-03-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocksearch', '0007_auto_20200308_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='mystock',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
