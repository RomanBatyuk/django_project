from django.db import models


class Publication(models.Model):
    headline = models.CharField(max_length=30, verbose_name="Заголовок")
    contents = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="images/", null=True, blank=True, verbose_name="Фотография"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    number_of_views = models.IntegerField(default=0, verbose_name="Счетчик просмотров")

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
