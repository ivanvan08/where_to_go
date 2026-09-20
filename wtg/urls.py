from django.urls import path

from . import views

urlpatterns = [
    path("", views.place_list, name="place_list"),
    path("add/", views.place_add, name="place_add"),
    path("<int:place_id>/", views.place_detail, name="place_detail"),
]
