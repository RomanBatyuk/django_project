from django.urls import include, path

from catalog.apps import CatalogConfig
from catalog.views import contacts, feedback, home, info_products, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("feedback/", feedback, name="feedback"),
    path('', info_products, name="info_products"),
    path('catalog/<int:pk>/', product_detail, name="product_detail"),
]