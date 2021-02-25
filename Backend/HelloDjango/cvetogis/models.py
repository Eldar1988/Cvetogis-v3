from django.db import models
from shop.models import City


class HomePageInfo(models.Model):
    """CEO информация для главной страницы"""
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Город')
    site_title = models.CharField('Заголовок для страницы города', max_length=110,
                                  help_text='Будет также использован в сео')
    site_description = models.TextField('Описание - description (SEO)')

    def __str__(self):
        return self.site_title

    class Meta:
        verbose_name = 'Информация для главной страницы магазина'
        verbose_name_plural = 'Информация для главных страниц магазина'
