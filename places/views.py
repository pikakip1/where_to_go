from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder


def serialized_info(places):
    cards_places = {
        'type': 'FeatureCollection',
        'features': []
    }

    for place in places:
        post = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng_coordinates, place.lat_coordinates]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_page', args=[place.id])
            }
        }
        cards_places['features'].append(post)
    return cards_places


def index(request):
    context = {
        'places': serialized_info(Place.objects.all())
    }
    return render(request, 'index.html', context)


def place_page(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    context = {
        'title': place.title,
        'imgs': [f'..{img.image.url}' for img in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        "coordinates": {
            "lng": place.lng_coordinates,
            "lat": place.lat_coordinates
        }
    }
    return JsonResponse(
        context,
        encoder=DjangoJSONEncoder,
        safe=False,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 4,
        }
    )
