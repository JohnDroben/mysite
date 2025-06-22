# Блог на Django
##  Проект представляет собой полнофункциональный блог с системой аутентификации пользователей, созданный на Django.

![2025-06-22_16-48-02](https://github.com/user-attachments/assets/1c0ad535-c349-4f71-84ac-c8341e870bd2)

## Основные функции

- 📝 Создание, редактирование и удаление постов
- 💬 Комментирование постов
- 👤 Регистрация и аутентификация пользователей
- 🔐 Профиль пользователя
- 🏷️ Избранные посты
- 🖼️ Загрузка изображений для постов

## Технологии

- Python 3.10+
- Django 5.2
- SQLite (для разработки)
- Bootstrap 5 (для интерфейса)

## Структура проекта
```
mysite/
├── manage.py
├── db.sqlite3
├── __init__.py
├── users/               # Приложение для работы с пользователями
├── static/              # Статические файлы (CSS, JS, изображения)
├── mysite/              # Настройки проекта
├── media/               # Загруженные медиафайлы
├── blog/                # Приложение блога
│   ├── migrations/      # Миграции базы данных
│   ├── templates/       # Шаблоны блога
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── authentication/      # Приложение аутентификации
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── templates/           # Глобальные шаблоны
```

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/ваш-репозиторий.git
cd mysite
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

6. Запустите сервер разработки:
```bash
python manage.py runserver
```

7. Откройте в браузере:
```
http://localhost:8000/
```

## Настройки окружения

Создайте файл `.env` в корне проекта со следующими переменными:
```ini
DEBUG=True
SECRET_KEY=ваш-секретный-ключ
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Основные команды

- Запуск тестов: `python manage.py test`
- Создание миграций: `python manage.py makemigrations`
- Запуск shell: `python manage.py shell`
- Запуск production сервера: `python manage.py runserver 0.0.0.0:8000`

## Деплой в продакшн

1. Установите PostgreSQL вместо SQLite
2. Настройте `settings.py`:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['ваш-домен.com']
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'mydatabase',
           'USER': 'mydatabaseuser',
           'PASSWORD': 'mypassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
3. Соберите статические файлы:
   ```bash
   python manage.py collectstatic
   ```
4. Используйте Gunicorn или uWSGI для запуска

## Авторы

- [Geore Drobenuyk](https://github.com/JohnDroben)

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT - подробности см. в файле [LICENSE](LICENSE).
```
