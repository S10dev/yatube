# Generated by Django 2.2.9 on 2021-03-07 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_auto_20210307_0840'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-id']},
        ),
    ]
