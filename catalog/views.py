from gc import get_objects

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def feedback(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")


def info_products(request):
    product = Product.objects.all()
    context = {"product": product}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)
