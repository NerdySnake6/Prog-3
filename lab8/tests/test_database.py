"""Тесты CRUD-операций SQLite."""

import sqlite3
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from myapp.controllers.databaseController import CurrencyRatesCRUD
from myapp.models import Currency


class DatabaseTests(unittest.TestCase):
    """Проверяет работу с базой данных в памяти."""

    def setUp(self) -> None:
        """Создать новую базу для каждого теста."""
        self.connection = sqlite3.connect(":memory:")
        self.db = CurrencyRatesCRUD(self.connection)
        self.db.create_tables()

    def tearDown(self) -> None:
        """Закрыть подключение к базе."""
        self.connection.close()

    def test_create_and_read_currency(self) -> None:
        """CRUD-контроллер должен добавлять и читать валюту."""
        currency = Currency("840", "USD", "Доллар США", 90.0, 1)

        currency_id = self.db._create(currency)
        currencies = self.db._read()

        self.assertEqual(currency_id, 1)
        self.assertEqual(currencies[0]["char_code"], "USD")

    def test_update_currency(self) -> None:
        """Курс валюты должен обновляться по char_code."""
        self.db._create(Currency("978", "EUR", "Евро", 91.0, 1))

        updated = self.db._update({"EUR": 95.5})
        currency = self.db.get_currency_by_char_code("EUR")

        self.assertEqual(updated, 1)
        self.assertIsNotNone(currency)
        self.assertEqual(currency["value"], 95.5)

    def test_delete_currency(self) -> None:
        """Валюта должна удаляться по id."""
        currency_id = self.db._create(Currency("156", "CNY", "Юань", 12.5, 1))

        deleted = self.db._delete(currency_id)
        currencies = self.db._read()

        self.assertTrue(deleted)
        self.assertEqual(currencies, [])

    def test_user_subscriptions(self) -> None:
        """После seed_data пользователь должен иметь подписки."""
        self.db.seed_data()

        user = self.db.get_user(1)
        currencies = self.db.get_user_currencies(1)

        self.assertIsNotNone(user)
        self.assertEqual(len(currencies), 2)


if __name__ == "__main__":
    unittest.main()

