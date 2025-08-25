from django.urls import include, path

from catalog.apps import CatalogConfig
from catalog.views import ContactsView, FeedbackView, HomeView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path('', ProductListView.as_view(), name="product_list"),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
]