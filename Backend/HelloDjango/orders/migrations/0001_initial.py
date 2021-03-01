# Generated by Django 3.1.7 on 2021-03-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('complete', models.BooleanField(default=False, verbose_name='Обработано')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметка')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Обновлена')),
            ],
            options={
                'verbose_name': 'Заявка на обратный звонок',
                'verbose_name_plural': 'Заявки на обратный звонок',
                'ordering': ['-date'],
            },
        ),
    ]