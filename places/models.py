from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Описание')
    lng_coordinates = models.DecimalField(max_digits=12, decimal_places=10, verbose_name='Долгота')
    lat_coordinates = models.DecimalField(max_digits=12, decimal_places=10, verbose_name='Ширина')

    def __str__(self):
        return self.title
