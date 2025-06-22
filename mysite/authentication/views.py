from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm  # Создайте кастомную форму!

# Используем кастомную модель пользователя
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    """Главная страница"""
    return render(request, 'auth/index.html')


def login_view(request):
    """Вход пользователя"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"Добро пожаловать, {user.username}!")
            return redirect('auth:profile')
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})


@login_required
def logout_view(request):
    """Выход пользователя"""
    auth_logout(request)
    messages.info(request, "Вы успешно вышли из системы.")
    return redirect('auth:index')


class ProfileView(LoginRequiredMixin, TemplateView):
    """Профиль пользователя"""
    template_name = 'auth/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


def register(request):
    """Регистрация нового пользователя"""
    if request.method == 'POST':
        # Используем кастомную форму!
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Автоматический вход после регистрации
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('auth:profile')  # Перенаправление на страницу профиля
    else:
        form = CustomUserCreationForm()

    return render(request, 'auth/register.html', {'form': form})










