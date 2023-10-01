# django_template

## 1) Создание репозитория на github и проекта в pycharm, настройка виртуального окружения

Создаем проект, виртуальное окружение с помощью pyenv, создаем репозиторий на гитхабе.

Pyenv:
Открываем консоль, вводим pyenv. Он не видит команду, копируем туда:

    export PATH="~/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

Далее создаем виртуальное окружение для проекта:

    pyenv virtualenv 3.11.5 name_project

Просмотреть созданные окружения:

    pyenv versions

Выбираем в pycharm этот созданный интерпретатор. Выбираем в папке bin python3.

## 2) Настройка git

В проекте ничего не делаем, копируем следующие строки с нового репозитория github:

    echo "# dj_interview_3" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin git@github.com:Tework123/name_project.git
    git push -u origin main

Пояснение:

- создаем файл readme
- инициализируем пустой репозиторий гит
- добавляем в индекс файл
- делаем коммит
- переименовываем ветку
- соединяем локальный и внешний репозитории
- пушим локальные изменения во внешний репозиторий

Добавляем в проект .gitignore и копируем туда все с шаблонного проекта.

## 3) Django

Устанавливаем следующие пакеты в интерпретатор:

    pip install Django djangorestframework gunicorn
    "psycopg[binary]" python-dotenv whitenoise drf-yasg
    django-debug-toolbar celery django-phonenumber-field
    django-phonenumbers flower Faker Pillow redis
    django-cors-headers flake8

Создаем django проект:

    django-admin startproject name_my_site

Меняем один settings файл на несколько:

- base.py
- development.py
- production.py

Меняем название проекта в пути к urls и к wsgi в base.py.
Потом также с приложениями.

В настройках поменять тайм зону и язык.

    TIME_ZONE = 'Europe/Moscow'

Добавляем в верхнюю папку .env файл.

## 4) Подключение базы данных postgres

Создаем базу данных из pg-admin.

Подключаем ее в production.py и development.py и меняем название в .env:

    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_rest',
        'USER': 'postgres',
        'PASSWORD': 'ksflkOkas23fl9saflKdl349sLfsk1',
        'HOST': 'localhost',
        'PORT': '',
    }

}

Изменить название базы!!!

Меняем manage.py, также меняем путь к settings.

## 5) Переписываем стандартную модель пользователя

Создаем django-app:

    python3 manage.py startapp account

В нем будет модель пользователя и все связанное с ней.

Добавляем код в managers.py, admin.py, model.py

## 6) Прочие настройки

Добавляем все url в urls name_project. В том числе и панель дебаггера, а то будет ошибка.

Также создаем папку tests и файлы urls.py, serializer.py.
Создаем setup.cfg для flake8.

### Сделать миграции:

    python3 manage.py makemigrations
    python3 manage.py migrate

Отметить папку после backend как синий root в pycharm, перезапустить pycharm.

Проверить работу сервера, зайти в админку.

Запустить сервер:

    python manage.py runserver

Создать админа:

    python manage.py createsuperuser

Очистить базу:

    python manage.py flush

Если все работает, то сделать в папке с manage.py написать команду:

    pip freeze > requirements.txt

Далее создаем нужные приложения:

    python manage.py startapp name

И регистрируем их в settings:

    'account.apps.AccountConfig'





