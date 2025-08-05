from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, feedback

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback')
]