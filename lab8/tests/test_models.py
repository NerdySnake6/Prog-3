"""Тесты моделей лабораторной работы 8."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from myapp.models import Currency, User, UserCurrency


class ModelTests(unittest.TestCase):
    """Проверяет простую валидацию моделей."""

    def test_currency_valid_data(self) -> None:
        """Валюта должна сохранять корректные данные."""
        currency = Currency("840", "usd", "Доллар США", 90.0, 1)

        self.assertEqual(currency.char_code, "USD")
        self.assertEqual(currency.value, 90.0)

    def test_currency_bad_char_code(self) -> None:
        """Код валюты должен состоять из трех символов."""
        with self.assertRaises(ValueError):
            Currency("840", "US", "Доллар США", 90.0, 1)

    def test_currency_bad_value(self) -> None:
        """Курс валюты не может быть отрицательным."""
        with self.assertRaises(ValueError):
            Currency("840", "USD", "Доллар США", -1.0, 1)

    def test_user_validation(self) -> None:
        """Имя пользователя не должно быть пустым."""
        with self.assertRaises(ValueError):
            User("")

    def test_user_currency_validation(self) -> None:
        """Связь пользователя и валюты должна проверять id."""
        relation = UserCurrency(user_id=1, currency_id=2)

        self.assertEqual(relation.user_id, 1)
        with self.assertRaises(ValueError):
            relation.currency_id = 0


if __name__ == "__main__":
    unittest.main()

