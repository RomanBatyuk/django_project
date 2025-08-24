from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse
from blog.models import Publication
from django.shortcuts import render


class PublicationCreateView(CreateView):
    model = Publication
    fields = ["headline", "contents", "image"]
    template_name = "blog/publication_form.html"
    success_url = reverse_lazy("blog:blog_list")


class PublicationListView(ListView):
    model = Publication
    template_name = "blog/publication_list.html"
    context_object_name = "publication"

    def blog_list(request):
        published = Publication.objects.filter(published=True)
        return render(request, 'blog/blog_list.html', {'object_list': published})


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'blog/publication_detail.html'
    context_object_name = 'publication'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class PublicationUpdateView(UpdateView):
    model = Publication
    fields = ["headline", "contents", "image"]
    template_name = 'blog/publication_form.html'
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class PublicationDeleteView(DeleteView):
    model = Publication
    template_name = 'blog/publication_confirm_delete.html'
    success_url = reverse_lazy("blog:blog_list")
