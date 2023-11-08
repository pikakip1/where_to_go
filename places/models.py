from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    place_id = models.CharField(max_length=50, verbose_name='id')
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Описание')
    lng_coordinates = models.DecimalField(max_digits=12, decimal_places=10, verbose_name='Долгота')
    lat_coordinates = models.DecimalField(max_digits=12, decimal_places=10, verbose_name='Ширина')

    def __str__(self):
        return self.title


class PlaceImg(models.Model):
    location_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='place_img', verbose_name='Фото места', blank=True)

    def __str__(self):
        return self.location_name
