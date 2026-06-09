"""Контроллер бизнес-логики для валют."""

from myapp.controllers.databaseController import CurrencyRatesCRUD
from myapp.models import Currency


class CurrenciesController:
    """Работает с валютами через контроллер базы данных."""

    def __init__(self, db_controller: CurrencyRatesCRUD) -> None:
        """Создать контроллер валют."""
        self.db = db_controller

    def create_currency(
        self,
        num_code: str,
        char_code: str,
        name: str,
        value: float,
        nominal: int,
    ) -> int:
        """Добавить новую валюту."""
        currency = Currency(
            num_code=num_code,
            char_code=char_code,
            name=name,
            value=value,
            nominal=nominal,
        )
        return self.db._create(currency)

    def list_currencies(self) -> list[dict[str, int | str | float]]:
        """Вернуть список валют."""
        return self.db._read()

    def update_currency(self, char_code: str, value: float) -> int:
        """Обновить курс валюты."""
        return self.db._update({char_code: value})

    def delete_currency(self, currency_id: int) -> bool:
        """Удалить валюту."""
        return self.db._delete(currency_id)

    def show_currencies(self) -> list[dict[str, int | str | float]]:
        """Вывести валюты в консоль и вернуть их списком."""
        currencies = self.list_currencies()
        for currency in currencies:
            print(currency)
        return currencies

