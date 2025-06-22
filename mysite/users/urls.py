from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user_list'),  # Список пользователей
    path('<str:username>/', views.user_profile, name='user_profile'),  # Профиль
]
