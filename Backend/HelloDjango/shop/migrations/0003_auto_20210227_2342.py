# Generated by Django 3.1.7 on 2021-02-27 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210227_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='short_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='sort',
            name='description',
        ),
        migrations.RemoveField(
            model_name='sort',
            name='miniature',
        ),
        migrations.RemoveField(
            model_name='sort',
            name='public',
        ),
    ]