from django.contrib import admin

from blog.models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    exclude = ('published', 'number_of_views')
    list_display = ("headline", "contents", "image", "created_at", "number_of_views")
