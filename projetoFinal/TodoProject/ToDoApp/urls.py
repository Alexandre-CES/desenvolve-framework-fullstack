from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
  path('', views.index, name='index'),
  path('register', views.register, name='register'),
  path('login/', LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
  path('tasks/', views.task_list, name='task_list'),
  path('tasks/create/', views.task_create, name='task_create'),
  path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
  path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
  
]