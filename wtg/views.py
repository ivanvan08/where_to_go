from copy import deepcopy

from django.http import Http404
from django.shortcuts import render

from .data import DEFAULT_PLACES, with_stars


def get_places(request):
    if "places" not in request.session:
        request.session["places"] = deepcopy(DEFAULT_PLACES)
    return request.session["places"]


def place_list(request):
    places = get_places(request)
    items = [with_stars(place) for place in places]
    return render(request, "wtg/place_list.html", {"places": items})


def place_detail(request, place_id):
    places = get_places(request)
    place = None
    for p in places:
        if p["id"] == place_id:
            place = p
            break
    if place is None:
        raise Http404("Місце не знайдено")
    place = with_stars(place)
    return render(request, "wtg/place_detail.html", {"place": place})
