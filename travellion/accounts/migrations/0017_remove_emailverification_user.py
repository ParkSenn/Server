# Generated by Django 4.0.4 on 2023-09-23 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_emailverification_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailverification',
            name='user',
        ),
    ]
