from django.urls import path
from . import views
from .views import PostUpdateView, PostDeleteView, PostCreateView


app_name = 'blog'

urlpatterns = [
    path('', views.post_home, name='post_home'),  # Главная страница блога
    path('posts/', views.post_list, name='post_list'),  # Список всех постов
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Детали конкретного поста
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  # Создание нового поста
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),  # Обновление поста
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Удаление поста

]