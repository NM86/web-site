from django.db import models

class Articles(models.Model):
    title = models.CharField('', max_length=40)
    anons = models.CharField('Анонс', max_length=200)
    full_text = models.TextField('Публикация')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Записи'
        verbose_name_plural = 'Записи'