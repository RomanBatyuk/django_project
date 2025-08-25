from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from  django.views.generic import ListView, DetailView, TemplateView, View


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class FeedbackView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")

    def get(self, request, *args, **kwargs):
        return render(request, "catalog/contacts.html")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
