from django.db import models


class Course(models.Model):
    """Курсы валют"""
    title = models.CharField('Валюта', max_length=10)
    value = models.DecimalField('Курс (1 ед. валюты в тенге)', max_digits=6, decimal_places=2, default=0)
    abbr = models.CharField('Аббревиатура', max_length=5, default='тг')
    update = models.DateTimeField('Обновлено', auto_now=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы валют'
        ordering = ('order',)
