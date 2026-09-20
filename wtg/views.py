from copy import deepcopy

from django.shortcuts import render

from .data import DEFAULT_PLACES, rating_stars


def get_places(request):
    if "places" not in request.session:
        request.session["places"] = deepcopy(DEFAULT_PLACES)
    return request.session["places"]


def place_list(request):
    places = get_places(request)
    items = [{**place, "stars": rating_stars(place["rating"])} for place in places]
    return render(request, "wtg/place_list.html", {"places": items})
