"""Контроллер страницы со списком валют."""

from jinja2 import Environment

from myapp.controllers.data import FALLBACK_CURRENCIES, MAIN_APP, NAVIGATION
from myapp.models import Currency
from myapp.utils.currencies_api import CurrencyApiError, get_currencies


def load_currencies() -> tuple[list[Currency], str | None]:
    """Получить валюты или вернуть учебные данные при ошибке."""
    try:
        return get_currencies(), None
    except CurrencyApiError as error:
        return FALLBACK_CURRENCIES, str(error)


def show_currencies(env: Environment) -> str:
    """Сформировать HTML страницы валют."""
    currencies, error_message = load_currencies()
    template = env.get_template("currencies.html")
    return template.render(
        app=MAIN_APP,
        navigation=NAVIGATION,
        currencies=currencies,
        error_message=error_message,
    )

