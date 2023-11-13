import os
import requests
import json
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from places.models import PlaceImg, Place
from django.core.files.base import ContentFile
from where_to_go import settings


class Command(BaseCommand):
    def load_img(self, place, urls):
        for position, url in enumerate(urls):
            response_url = requests.get(url).content
            img_obj = PlaceImg()
            img_obj.image.save('load.jpg', ContentFile(response_url), save=False)
            img_obj.location_name = place
            img_obj.position = position
            img_obj.save()

    def handle(self, *args, **options):
        json_places = os.listdir(settings.LOAD_ROOT)
        for place in json_places:
            with open(f'{settings.LOAD_ROOT}/{place}', 'r', encoding='utf-8') as json_file:
                json_place = json.load(json_file)

                try:
                    place_obj, created = Place.objects.get_or_create(
                        title=json_place['title'],
                        description_short=json_place['description_short'],
                        description_long=json_place['description_long'],
                        lng_coordinates=json_place['coordinates']['lng'],
                        lat_coordinates=json_place['coordinates']['lat'],
                    )
                    if created:
                        self.load_img(Place.objects.get(id=place_obj.id), json_place['imgs'])

                except IntegrityError:
                    print(f'Запись {json_place["title"]} существует')




