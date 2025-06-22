from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


User = get_user_model()  # Получаем активную модель пользователя

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/user_profile.html', {'user': user})

# Create your views here.
