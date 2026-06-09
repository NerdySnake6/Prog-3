"""Тесты функции получения валют."""

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from myapp.utils.currencies_api import CurrencyApiError, get_currencies


class FakeResponse:
    """Простой объект вместо ответа urllib."""

    def __init__(self, data: bytes) -> None:
        """Сохранить XML-данные."""
        self.data = data

    def __enter__(self) -> "FakeResponse":
        """Вернуть себя для with."""
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Закрытие здесь не требуется."""

    def read(self) -> bytes:
        """Вернуть подготовленные данные."""
        return self.data


class CurrencyApiTests(unittest.TestCase):
    """Проверяет разбор XML с курсами валют."""

    def test_get_currencies_parses_xml(self) -> None:
        """Функция должна создавать Currency из XML."""
        xml_data = """
        <ValCurs>
            <Valute ID="R01280">
                <NumCode>360</NumCode>
                <CharCode>IDR</CharCode>
                <Nominal>10000</Nominal>
                <Name>Рупий</Name>
                <Value>48,6178</Value>
            </Valute>
        </ValCurs>
        """.encode("utf-8")

        with patch(
            "myapp.utils.currencies_api.urlopen",
            return_value=FakeResponse(xml_data),
        ):
            currencies = get_currencies()

        self.assertEqual(len(currencies), 1)
        self.assertEqual(currencies[0].char_code, "IDR")
        self.assertEqual(currencies[0].value, 48.6178)

    def test_get_currencies_raises_for_empty_xml(self) -> None:
        """Пустой список валют должен считаться ошибкой."""
        with patch(
            "myapp.utils.currencies_api.urlopen",
            return_value=FakeResponse(b"<ValCurs></ValCurs>"),
        ):
            with self.assertRaises(CurrencyApiError):
                get_currencies()


if __name__ == "__main__":
    unittest.main()

