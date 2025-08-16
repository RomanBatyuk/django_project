from django.urls import include, path

from catalog.apps import CatalogConfig
from catalog.views import contacts, feedback, home

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("feedback/", feedback, name="feedback"),
]