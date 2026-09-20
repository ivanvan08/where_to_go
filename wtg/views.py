from copy import deepcopy
from datetime import date

from django.http import Http404
from django.shortcuts import redirect, render

from .data import DEFAULT_PLACES, pick_random, with_stars
from .forms import PlaceForm


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


def home(request):
    place = None
    if request.GET.get("random"):
        places = get_places(request)
        place = with_stars(pick_random(places))
    return render(request, "wtg/home.html", {"place": place})


def place_add(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            places = get_places(request)
            new_id = max((p["id"] for p in places), default=0) + 1
            places.append(
                {
                    **form.cleaned_data,
                    "id": new_id,
                    "created": date.today().isoformat(),
                }
            )
            request.session.modified = True
            return redirect("place_list")
    else:
        form = PlaceForm()
    return render(request, "wtg/place_add.html", {"form": form})
