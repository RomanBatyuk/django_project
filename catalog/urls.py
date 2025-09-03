from django.urls import include, path

from catalog.apps import CatalogConfig
from catalog.views import ContactsView, FeedbackView, HomeView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductUnpublishView

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path('catalog/', ProductListView.as_view(), name="product_list"),
    path('catalog/new/', ProductCreateView.as_view(), name="product_form"),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
    path('catalog/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/unpublish/', ProductUnpublishView.as_view(), name='product_unpublish'),
]