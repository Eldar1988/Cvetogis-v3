# Generated by Django 3.1.7 on 2021-02-27 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(verbose_name='')),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Порядковый номер')),
            ],
            options={
                'verbose_name': 'Категория подарка',
                'verbose_name_plural': 'Категории подарков',
                'ordering': ('order',),
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='cities',
        ),
        migrations.AddField(
            model_name='product',
            name='cities',
            field=models.ManyToManyField(blank=True, related_name='products', to='shop.City', verbose_name='Наличие в городах'),
        ),
        migrations.AddField(
            model_name='product',
            name='present_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='presents', to='shop.presentcategory', verbose_name='Категория подарков'),
        ),
    ]