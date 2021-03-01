from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField


class City(models.Model):
    """Города"""
    title = models.CharField('Название города', max_length=255)
    slug = models.SlugField(unique=True)
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


class Reason(models.Model):
    """Повод для букета"""
    title = models.CharField('Название повода', max_length=255)
    icon = models.CharField('Иконка', default='mdi-', max_length=100, help_text='https://materialdesignicons.com/')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Повод'
        verbose_name_plural = 'Поводы'
        ordering = ('order',)


class Sort(models.Model):
    """Сорта цветов"""
    title = models.CharField('Название сорта', max_length=255)
    order = models.PositiveSmallIntegerField('Порядковый номер', blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сорт'
        verbose_name_plural = 'Сорта'
        ordering = ('order',)


class Recommendation(models.Model):
    """Рекомендации к цветам"""
    title = models.CharField('Заголовок', max_length=255)
    image = CloudinaryField('Миниатюра', folder='cvetogis/recommendations')
    text = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекомендации'


class Seller(models.Model):
    """Продавцы"""
    title = models.CharField('Название продавца', max_length=255)
    phone = models.CharField('Номер телефона', max_length=30)
    address = models.TextField('Адрес магазина', blank=True, null=True)
    info = models.TextField('Дополнительная информация', blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


class PresentCategory(models.Model):
    """Категория для подарков"""
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория подарка'
        verbose_name_plural = 'Категории подарков'
        ordering = ('order',)


class People(models.Model):
    """Люди (для кого цветы)"""
    title = models.CharField('Заголовок', max_length=255)
    icon = models.CharField('Иконка', default='mdi-', max_length=200, help_text='https://materialdesignicons.com/')
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кому'
        verbose_name_plural = 'Кому'
        ordering = ('order',)


class Product(models.Model):
    """Товары"""
    title = models.CharField('Название товара', max_length=255, db_index=True)
    cities = models.ManyToManyField(City, blank=True, related_name='products', verbose_name='Наличие в городах')
    present_category = models.ForeignKey(PresentCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='presents', verbose_name='Категория подарков')
    recommendation = models.ForeignKey(Recommendation, on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='products', verbose_name='Рекомендация')
    sort = models.ManyToManyField(Sort, blank=True, related_name='products', verbose_name='Сорт')
    reasons = models.ManyToManyField(Reason, blank=True, related_name='products', verbose_name='Повод')
    flowers_for = models.ManyToManyField(People, blank=True, related_name='products', verbose_name='Для кого')
    price = models.IntegerField('Цена товара')
    old_price = models.IntegerField('Старая цена товара(необязательно)', blank=True, null=True)
    miniature = CloudinaryField('Миниатюра', folder='cvetogis/products', blank=True, null=True)
    image = CloudinaryField('Основное изображение товара', folder='cvetogis/products')
    rating = models.PositiveSmallIntegerField('Рейтинг товара', default=5)
    description = models.TextField('Краткое описание товара')
    delivery = models.TextField('Условия доставки', null=True, blank=True)
    composition = models.TextField('Состав', null=True, blank=True)
    note = models.TextField('Примечание', null=True, blank=True)
    # Booleans
    future = models.BooleanField('Рекомендуем', default=False)
    flower = models.BooleanField('Цветы', default=False)
    bouquet = models.BooleanField('Букеты', default=False)
    present = models.BooleanField('Подарок', default=False)
    in_the_box = models.BooleanField('В коробке', default=False)
    set = models.BooleanField('Набор', default=False)
    show_on_home_page = models.BooleanField('На главной', default=False)

    order = models.PositiveSmallIntegerField('Порядковый номер', blank=True, null=True)
    slug = models.SlugField('Slug', unique=True)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, verbose_name='Продавец', null=True, blank=True,
                               related_name='products')
    public = models.BooleanField('Опубликовать', default=True)
    views = models.PositiveSmallIntegerField('Количество просмотров', default=0)
    pub_date = models.DateTimeField('Опубликован', auto_now_add=True)
    update = models.DateTimeField('Изменен', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('order', 'price')


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='images', verbose_name='Товар')
    image = CloudinaryField('Дополнительные изображения товара', folder='cvetogis/products/images')

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'
