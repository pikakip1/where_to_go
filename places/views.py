from django.shortcuts import render
from places.models import Place, PlaceImg


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
                    'coordinates': [place.lng_coordinates, place.lat_coordinates,]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.place_id,
                    'detailsUrl': f'static/places/{place.place_id}.json'
                }
            }

        cards_places['features'].append(post)
    return cards_places


def index(request):
    context = {
        'places': serialized_info(Place.objects.all())
    }

    return render(request, 'index.html', context)
