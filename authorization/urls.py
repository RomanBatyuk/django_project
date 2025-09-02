from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from authorization.views import RegisterView

app_name = 'authorization'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='authorization/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
