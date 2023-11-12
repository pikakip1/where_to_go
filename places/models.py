from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Описание')
    lng_coordinates = models.DecimalField(max_digits=12, decimal_places=10, verbose_name='Долгота')
    lat_coordinates = models.DecimalField(max_digits=12, decimal_places=10, verbose_name='Ширина')

    def __str__(self):
        return self.title


class PlaceImg(models.Model):
    location_name = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='place_img', verbose_name='Фото', blank=True)
    position = models.PositiveIntegerField(verbose_name='Позиция', null=True)

    def __str__(self):
        return f'{self.location_name}'
