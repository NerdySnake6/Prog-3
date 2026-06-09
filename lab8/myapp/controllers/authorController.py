"""Данные об авторе и приложении."""

from myapp.models import App, Author

MAIN_AUTHOR = Author(name="Калинин Игорь", group="ИВТ-2")
MAIN_APP = App(name="CurrencyCrudApp", version="1.0", author=MAIN_AUTHOR)

NAVIGATION = [
    {"caption": "Главная", "href": "/"},
    {"caption": "Пользователи", "href": "/users"},
    {"caption": "Валюты", "href": "/currencies"},
    {"caption": "Автор", "href": "/author"},
]
