from django.urls import path
from blog.apps import BlogConfig
from blog.views import PublicationListView, PublicationDetailView, PublicationCreateView, PublicationUpdateView, PublicationDeleteView

app_name = BlogConfig.name


urlpatterns = [
    path('blog/', PublicationListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', PublicationDetailView.as_view(), name='blog_detail'),
    path('blog/new/', PublicationCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit/', PublicationUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete/', PublicationDeleteView.as_view(), name='blog_delete'),
]