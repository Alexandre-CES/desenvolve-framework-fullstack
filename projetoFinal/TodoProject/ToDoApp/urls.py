from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
  path('', views.index, name='index'),
  path('register', views.register, name='register'),
  path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]