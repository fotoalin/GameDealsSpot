from django.urls import include, path

from . import views

app_name = "deals"

urlpatterns = [
    path("", views.index, name="index"),
    path("deals/", views.deals, name="deals"),
    path("filter/", views.filter, name="filter"),
    path("search/", views.search, name="search"),
    path("contact/", views.contact, name="contact"),
]
