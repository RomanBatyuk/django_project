from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.forms import ProductForm
from catalog.models import Product

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect



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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Форма невалидна:", form.errors)
        return super().form_invalid(form)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = "product"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:product_list")
    permission_required = 'catalog.change_product'

    def has_permission(self):
        """
        Переопределяем проверку прав: пользователь должен иметь глобальное право
        ИЛИ быть владельцем продукта.
        """
        # Сначала проверяем глобальное право
        has_global_perm = super().has_permission()
        if has_global_perm:
            return True  # Админ или пользователь с правом может редактировать всё

        # Если нет глобального права, проверяем, является ли пользователь владельцем
        obj = get_object_or_404(Product, pk=self.kwargs['pk'])
        return self.request.user == obj.owner



class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy("catalog:product_list")
    permission_required = 'catalog.delete_product'

    def has_permission(self):
        # Проверяем глобальное право
        has_global_perm = super().has_permission()
        if has_global_perm:
            return True

        # Проверяем, является ли пользователь владельцем продукта
        obj = get_object_or_404(Product, pk=self.kwargs['pk'])
        return self.request.user == obj.owner


class ProductUnpublishView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = []  # Нет полей для редактирования — форма пустая
    template_name = 'catalog/product_confirm_unpublish.html'  # Шаблон подтверждения
    success_url = reverse_lazy('catalog:product_list')  # Куда редирект после отмены публикации

    def form_valid(self, form):
        product = self.object
        user = self.request.user

        # Проверяем, владелец ли это продукта или модератор с нужным правом
        if product.owner == user or (
            user.groups.filter(name='Модератор продуктов').exists() and
            user.has_perm('catalog.cancellation_of_product')
        ):
            product.published = False
            product.save()
            return redirect(self.success_url)
        else:
            return HttpResponseForbidden("У вас нет прав отменять публикацию этого продукта")

    def get(self, request, *args, **kwargs):
        # Показываем страницу подтверждения отмены публикации
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        # Обрабатываем отправку формы (подтверждение)
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
