"""Тесты простой серверной маршрутизации."""

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from myapp.models import Currency
from myapp.myapp import build_response


def _demo_currencies() -> list[Currency]:
    """Вернуть валюты для тестов страниц."""
    return [
        Currency("R01235", "840", "USD", "Доллар США", 90.0, 1),
        Currency("R01239", "978", "EUR", "Евро", 97.0, 1),
    ]


class ServerTests(unittest.TestCase):
    """Проверяет ответы основных маршрутов."""

    def test_index_route(self) -> None:
        """Главная страница должна открываться."""
        status, content_type, body = build_response("/")

        self.assertEqual(status, 200)
        self.assertIn("text/html", content_type)
        self.assertIn("CurrenciesListApp", body.decode("utf-8"))

    def test_users_route(self) -> None:
        """Страница пользователей должна показывать список."""
        status, _, body = build_response("/users")

        self.assertEqual(status, 200)
        self.assertIn("Пользователи", body.decode("utf-8"))

    def test_currencies_route(self) -> None:
        """Страница валют должна показывать полученные курсы."""
        with patch(
            "myapp.controllers.currenciesController.get_currencies",
            return_value=_demo_currencies(),
        ):
            status, _, body = build_response("/currencies")

        html = body.decode("utf-8")
        self.assertEqual(status, 200)
        self.assertIn("USD", html)
        self.assertIn("EUR", html)

    def test_user_route(self) -> None:
        """Страница пользователя должна учитывать query-параметр id."""
        with patch(
            "myapp.controllers.currenciesController.get_currencies",
            return_value=_demo_currencies(),
        ):
            status, _, body = build_response("/user?id=1")

        html = body.decode("utf-8")
        self.assertEqual(status, 200)
        self.assertIn("Пользователь: Иван", html)
        self.assertIn("USD", html)

    def test_unknown_user_route(self) -> None:
        """Неизвестный пользователь должен давать 404."""
        status, _, body = build_response("/user?id=999")

        self.assertEqual(status, 404)
        self.assertIn("Пользователь не найден", body.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()

