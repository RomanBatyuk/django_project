from catalog.models import Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache
from django.views.generic import ListView



def get_product_list_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    product = cache.get(key)
    if product is not None:
        return product
    product = Product.objects.all()
    cache.set(key, product)
    return product


def get_category_product(category_id):
    return Product.objects.filter(category_id=category_id)

class ProductCategoryListView(ListView):
    model = Product
    template_name = "catalog/product_category_list.html"

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return get_category_product(category_id)