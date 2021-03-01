# Generated by Django 3.1.7 on 2021-03-01 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210228_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('icon', models.CharField(default='mdi-', help_text='https://materialdesignicons.com/', max_length=200, verbose_name='Иконка')),
                ('slug', models.SlugField(unique=True)),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Порядковый номер')),
            ],
            options={
                'verbose_name': 'Кому',
                'verbose_name_plural': 'Кому',
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='flowers_for',
            field=models.ManyToManyField(blank=True, related_name='products', to='shop.People', verbose_name='Для кого'),
        ),
    ]