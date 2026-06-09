"""Тесты моделей приложения."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from myapp.models import App, Author, Currency, User, UserCurrency


class ModelTests(unittest.TestCase):
    """Проверяет создание моделей и простую валидацию."""

    def test_author_and_app(self) -> None:
        """Автор и приложение должны сохранять переданные значения."""
        author = Author("Игорь", "ПРОГ-3")
        app = App("CurrenciesListApp", "1.0", author)

        self.assertEqual(app.name, "CurrenciesListApp")
        self.assertEqual(app.author.group, "ПРОГ-3")

    def test_user_validation(self) -> None:
        """Пользователь не должен создаваться с плохими данными."""
        with self.assertRaises(ValueError):
            User(0, "Иван")
        with self.assertRaises(ValueError):
            User(1, "")

    def test_currency_validation(self) -> None:
        """Валюта должна проверять курс и номинал."""
        currency = Currency("R01235", "840", "usd", "Доллар США", 90.0, 1)

        self.assertEqual(currency.char_code, "USD")
        with self.assertRaises(ValueError):
            currency.value = 0
        with self.assertRaises(ValueError):
            currency.nominal = -1

    def test_user_currency_validation(self) -> None:
        """Связь пользователя и валюты должна проверять id."""
        relation = UserCurrency(1, 1, "R01235")

        self.assertEqual(relation.user_id, 1)
        with self.assertRaises(ValueError):
            relation.currency_id = ""


if __name__ == "__main__":
    unittest.main()

