from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField


class City(models.Model):
    """Города"""
    title = models.CharField('Название города', max_length=255)
    slug = models.SlugField(unique=True)
    address = models.TextField('Адрес магазина в городе', null=True, blank=True, help_text='Вместе с названием города')
    phone = models.CharField('Номер телефона', max_length=20, blank=True, null=True)
    whatsapp = models.CharField('Whatsapp', max_length=20, help_text='В формате: 7 707 *** ****', null=True, blank=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('order',)


class DeliveryBranch(models.Model):
    """Район доставки"""
    title = models.CharField('Название района', max_length=255)
    price = models.PositiveSmallIntegerField('Цена доставки',
                                             help_text='Необходимо добавить район с нулевой стоиомстью доставки')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries',
                             verbose_name='Город')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Район доставки'
        verbose_name_plural = 'Районы доставки'
        ordering = ('order',)


class Category(models.Model):
    """Категория"""
    title = models.CharField('Заголовок категории', max_length=255, db_index=True)
    image = CloudinaryField('Картинка категории', folder='cvetogis/categories')
    miniature = CloudinaryField('Миниатюра категории', folder='cvetogis/categories/miniatures')
    description = models.TextField('Описание категории')
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)
    cities = models.ManyToManyField(City, related_name='categories', verbose_name='Выберите города')
    show_on_home_page = models.BooleanField('Показать на главной странице', default=False)
    public = models.BooleanField('Опубликовать', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('order',)