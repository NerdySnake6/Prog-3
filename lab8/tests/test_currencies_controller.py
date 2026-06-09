"""Тесты контроллера валют с unittest.mock."""

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from myapp.controllers.currenciesController import CurrenciesController


class CurrenciesControllerTests(unittest.TestCase):
    """Проверяет вызовы контроллера базы через mock."""

    def test_list_currencies(self) -> None:
        """list_currencies должен вызывать _read."""
        mock_db = MagicMock()
        mock_db._read.return_value = [{"id": 1, "char_code": "USD"}]
        controller = CurrenciesController(mock_db)

        result = controller.list_currencies()

        self.assertEqual(result[0]["char_code"], "USD")
        mock_db._read.assert_called_once()

    def test_update_currency(self) -> None:
        """update_currency должен передавать словарь в _update."""
        mock_db = MagicMock()
        mock_db._update.return_value = 1
        controller = CurrenciesController(mock_db)

        result = controller.update_currency("USD", 100.0)

        self.assertEqual(result, 1)
        mock_db._update.assert_called_once_with({"USD": 100.0})

    def test_delete_currency(self) -> None:
        """delete_currency должен вызывать _delete."""
        mock_db = MagicMock()
        mock_db._delete.return_value = True
        controller = CurrenciesController(mock_db)

        result = controller.delete_currency(1)

        self.assertTrue(result)
        mock_db._delete.assert_called_once_with(1)


if __name__ == "__main__":
    unittest.main()

