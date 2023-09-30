### API_FINAL_YATUBE

#### 1) О проекте:
Данный API-сервис нацелен на любителей социальных сетей и общения. В данном сервисе реализован базовый функционал любой из современных социальных сетей, Вы сможете создавать публикации и комментировать публикации других пользователей, реализовано разбиение публикаций по разным тематическим группам, подписка на контент других пользователей и еще многое другое...)  

#### 2) Запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:timrybakov/api_final_yatube.git
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции и запустить проект:

```
python manage.py migrate
python manage.py runserver
```

#### 3) Вариации API-запросов:

* Запрос для создание пользователя:

```
Отправялем post-запрос по url-адресу: http://127.0.0.1:8000/api/v1/users/

{
    "username": "string",
    "password": "string"
}

Ответ:
{
    "id": int
    "user": "string",
    "following": "string"
}

```

* Получение JWT-токена:

```
Отправялем post-запрос по url-адресу: http://127.0.0.1:8000/api/v1/jwt/create/

Запрос:
{
    "username": "string",
    "password": "string"
}

Ответ:
{
    "refresh": "string",
    "access": "string"
}

Необходимо указать в заголовках токен доступа (access), без этого токена не будет предоставлен полный функционал сервиса !
```

* Получение всех публикаций:

```
Отправялем get-запрос по url-адресу: http://127.0.0.1:8000/api/v1/posts/

Ответ:
{
    "count": 123,
    "next": "http://127.0.0.1:8000/api/v1/posts/?offset=400&limit=100",
    "previous": "http://127.0.0.1:8000/api/v1/posts/?offset=200&limit=100",
    "results": [
        {}
    ]
}
```

* Создание комментария: 

```
Отправялем post-запрос по url-адресу: http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Запрос:
{
    "text": "string"
}

Ответ:
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```

* Получение всех подписок пользователя:

```
Отправялем get-запрос по url-адресу: http://127.0.0.1:8000/api/v1/follow/

Ответ:
[
    {
        "user": "string",
        "following": "string"
    }
]
