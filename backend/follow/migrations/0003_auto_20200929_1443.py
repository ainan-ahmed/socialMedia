# Generated by Django 2.2.16 on 2020-09-29 14:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('follow', '0002_auto_20200929_1431'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='following',
            unique_together={('user_id', 'following_user_id')},
        ),
    ]
