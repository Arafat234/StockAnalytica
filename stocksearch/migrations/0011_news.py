# Generated by Django 2.2 on 2020-03-11 16:11

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stocksearch', '0010_searchresults_field1'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsfield', jsonfield.fields.JSONField(blank=True, null=True)),
            ],
        ),
    ]
