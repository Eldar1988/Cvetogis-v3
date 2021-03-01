from django.db import models


class CallBack(models.Model):
    phone = models.CharField('Телефон', max_length=20)
    complete = models.BooleanField('Обработано', default=False)
    note = models.TextField('Заметка', null=True, blank=True)
    date = models.DateTimeField('Создана', auto_now_add=True)
    update = models.DateTimeField('Обновлена', auto_now=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Заявка на обратный звонок'
        verbose_name_plural = 'Заявки на обратный звонок'
        ordering = ['-date']
