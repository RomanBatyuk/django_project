from email.policy import default

from django.db import models

from authorization.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="images/", null=True, blank=True, verbose_name="Фотография"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    published = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

        permissions = [
            ("cancellation_of_product", "cancellation of product"),  # отмена публикации
        ]