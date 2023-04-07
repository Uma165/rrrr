from django.db import models

class Articles(models.Model):
    kind = models.CharField('Вид животного', max_length=50)
    name = models.CharField('Имя', max_length=250)
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата публикации')
    img = models.ImageField(upload_to='%Y/%m/%d', verbose_name='Фотография')

    def __str__(self):
        return self.kind

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name='Зверь'
        verbose_name_plural = 'Зверушки'