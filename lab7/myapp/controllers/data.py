"""Учебные данные для приложения."""

from myapp.models import App, Author, Currency, User, UserCurrency

MAIN_AUTHOR = Author(name="Калинин Игорь", group="ПРОГ-3")
MAIN_APP = App(name="CurrenciesListApp", version="1.0", author=MAIN_AUTHOR)

USERS = [
    User(user_id=1, name="Иван"),
    User(user_id=2, name="Анна"),
    User(user_id=3, name="Мария"),
]

USER_CURRENCIES = [
    UserCurrency(relation_id=1, user_id=1, currency_id="R01235"),
    UserCurrency(relation_id=2, user_id=1, currency_id="R01239"),
    UserCurrency(relation_id=3, user_id=2, currency_id="R01035"),
    UserCurrency(relation_id=4, user_id=3, currency_id="R01375"),
]

# Эти данные нужны, если сайт ЦБ РФ временно недоступен.
FALLBACK_CURRENCIES = [
    Currency("R01235", "840", "USD", "Доллар США", 89.50, 1),
    Currency("R01239", "978", "EUR", "Евро", 96.20, 1),
    Currency("R01035", "826", "GBP", "Фунт стерлингов", 113.40, 1),
    Currency("R01375", "156", "CNY", "Китайский юань", 12.30, 1),
]

NAVIGATION = [
    {"caption": "Главная", "href": "/"},
    {"caption": "Пользователи", "href": "/users"},
    {"caption": "Валюты", "href": "/currencies"},
    {"caption": "Автор", "href": "/author"},
]

