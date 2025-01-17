from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField
from django.db import models


class Slider(models.Model):
    """Основной слайдер"""
    title = models.CharField('Заголовок', max_length=110, db_index=True)
    image = CloudinaryField('Изображение', folder='cvetogis/slider')
    text = models.TextField('Текст-призыв')
    button_text = models.CharField('Текст на кнопке', max_length=55, default='Подробнее')
    button_url = models.CharField('Slug', max_length=255)
    order = models.PositiveSmallIntegerField('Порядковый номер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = '1. Слайдер'
        ordering = ('order',)


class PrivacyPolicy(models.Model):
    """Политика конфиденциальности"""
    title = models.CharField('Заголовок', max_length=100)
    text = RichTextUploadingField('Тектс')
    public = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = '6. Политика конфиденциальности'


class PublicOffer(models.Model):
    """Публичная оферта"""
    title = models.CharField('Заголовок', max_length=100)
    text = RichTextUploadingField('Тектс')
    public = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публичная оферта'
        verbose_name_plural = '5. Публичная оферта'


class ShippingAndPayment(models.Model):
    """Доставка и оплата"""
    title = models.CharField('Заголовок', max_length=100)
    text = RichTextUploadingField('Тектс')
    public = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = '4. Доставка'


class AboutInfo(models.Model):
    """Инофрмация о компании"""
    title = models.CharField('Заголовок', max_length=255, default='О нас')
    short_info = models.TextField('Краткая информация о компании', max_length=200, help_text='Будет отображаться на главной')
    info = RichTextUploadingField('Полное описание компании')
    requisite = RichTextUploadingField('Реквизиты компании')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = '2. О компании'


class Testimonial(models.Model):
    """Отзывы"""
    name = models.CharField('Имя', max_length=255)
    text = models.TextField('Отзыв')
    image = CloudinaryField('Фото', folder='cvetogis/testimonials', null=True, blank=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    public = models.BooleanField('Опубликовать', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = '3. Отзывы'
        ordering = ('-pub_date',)
