"""Контроллер страниц пользователей."""

from datetime import date

from jinja2 import Environment

from myapp.controllers.currenciesController import load_currencies
from myapp.controllers.data import MAIN_APP, NAVIGATION, USER_CURRENCIES, USERS
from myapp.models import Currency, User

MONTH_NAMES = [
    "январь",
    "февраль",
    "март",
    "апрель",
    "май",
    "июнь",
    "июль",
    "август",
    "сентябрь",
    "октябрь",
    "ноябрь",
    "декабрь",
]


def show_users(env: Environment) -> str:
    """Сформировать HTML страницы со списком пользователей."""
    template = env.get_template("users.html")
    return template.render(
        app=MAIN_APP,
        navigation=NAVIGATION,
        users=USERS,
    )


def show_user(env: Environment, query: dict[str, list[str]]) -> tuple[int, str]:
    """Сформировать HTML страницы одного пользователя."""
    user_id = _get_user_id(query)
    user = _find_user(user_id)

    if user is None:
        template = env.get_template("404.html")
        html = template.render(
            app=MAIN_APP,
            navigation=NAVIGATION,
            message="Пользователь не найден.",
        )
        return 404, html

    currencies, error_message = load_currencies()
    subscriptions = _get_user_currencies(user, currencies)
    chart_data = _make_chart_data(subscriptions)
    template = env.get_template("user.html")

    html = template.render(
        app=MAIN_APP,
        navigation=NAVIGATION,
        user=user,
        subscriptions=subscriptions,
        chart_data=chart_data,
        error_message=error_message,
    )
    return 200, html


def _get_user_id(query: dict[str, list[str]]) -> int:
    """Достать id пользователя из query-параметров."""
    try:
        return int(query.get("id", ["0"])[0])
    except ValueError:
        return 0


def _find_user(user_id: int) -> User | None:
    """Найти пользователя по id."""
    for user in USERS:
        if user.id == user_id:
            return user
    return None


def _get_user_currencies(
    user: User,
    currencies: list[Currency],
) -> list[Currency]:
    """Получить валюты, на которые подписан пользователь."""
    ids = [
        relation.currency_id
        for relation in USER_CURRENCIES
        if relation.user_id == user.id
    ]
    return [currency for currency in currencies if currency.id in ids]


def _last_three_months() -> list[str]:
    """Вернуть подписи последних трех месяцев."""
    today = date.today()
    labels = []
    for step in range(2, -1, -1):
        month_number = today.month - step
        year = today.year
        if month_number <= 0:
            month_number += 12
            year -= 1
        month_name = MONTH_NAMES[month_number - 1]
        labels.append(f"{month_name} {year}")
    return labels


def _make_chart_data(currencies: list[Currency]) -> dict[str, object]:
    """Подготовить простые данные для графика."""
    labels = _last_three_months()
    items = []

    for currency in currencies:
        # Для учебного графика делаем три точки вокруг текущего курса.
        values = [
            round(currency.value * 0.97, 4),
            round(currency.value * 1.02, 4),
            round(currency.value, 4),
        ]
        items.append(
            {
                "name": currency.char_code,
                "values": values,
            }
        )

    return {"labels": labels, "items": items}

