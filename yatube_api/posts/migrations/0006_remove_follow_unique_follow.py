# Generated by Django 3.2.16 on 2023-09-29 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_follow_unique_follow'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follow',
        ),
    ]
