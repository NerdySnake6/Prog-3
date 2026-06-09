"""Тесты GET-роутера приложения."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from myapp.myapp import create_router


class RouterTests(unittest.TestCase):
    """Проверяет основные маршруты приложения."""

    def setUp(self) -> None:
        """Создать свежий роутер с новой базой."""
        self.router = create_router()

    def test_index_route(self) -> None:
        """Главная страница должна открываться."""
        status, headers, body = self.router.handle("/")

        self.assertEqual(status, 200)
        self.assertIn("text/html", headers["Content-Type"])
        self.assertIn("CurrencyCrudApp", body.decode("utf-8"))

    def test_currencies_route(self) -> None:
        """Страница валют должна показывать таблицу."""
        status, _, body = self.router.handle("/currencies")

        html = body.decode("utf-8")
        self.assertEqual(status, 200)
        self.assertIn("USD", html)
        self.assertIn("EUR", html)

    def test_update_route(self) -> None:
        """Маршрут обновления должен менять курс валюты."""
        status, headers, _ = self.router.handle("/currency/update?USD=101")
        _, _, body = self.router.handle("/currencies")

        self.assertEqual(status, 302)
        self.assertIn("/currencies", headers["Location"])
        self.assertIn("101.00", body.decode("utf-8"))

    def test_delete_route(self) -> None:
        """Маршрут удаления должен удалять валюту."""
        status, headers, _ = self.router.handle("/currency/delete?id=1")
        _, _, body = self.router.handle("/currencies")

        self.assertEqual(status, 302)
        self.assertIn("/currencies", headers["Location"])
        self.assertNotIn("Доллар США", body.decode("utf-8"))

    def test_user_route(self) -> None:
        """Страница пользователя должна показывать подписки."""
        status, _, body = self.router.handle("/user?id=1")

        html = body.decode("utf-8")
        self.assertEqual(status, 200)
        self.assertIn("Пользователь: Иван", html)
        self.assertIn("USD", html)


if __name__ == "__main__":
    unittest.main()

