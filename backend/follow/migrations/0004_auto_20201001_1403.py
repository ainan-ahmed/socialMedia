# Generated by Django 2.2.16 on 2020-10-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0003_auto_20200929_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following',
            name='status',
            field=models.IntegerField(choices=[(1, 'Following'), (2, 'Blocked')], default=1),
        ),
    ]
