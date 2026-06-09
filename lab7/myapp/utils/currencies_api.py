"""Получение курсов валют из XML-сервиса ЦБ РФ."""

from urllib.error import URLError
from urllib.request import urlopen
from xml.etree import ElementTree

from myapp.models import Currency

CBR_DAILY_URL = "https://www.cbr.ru/scripts/XML_daily.asp"


class CurrencyApiError(Exception):
    """Ошибка при получении или разборе курсов валют."""


def _text(element: ElementTree.Element, tag: str) -> str:
    """Вернуть текст вложенного XML-тега."""
    node = element.find(tag)
    if node is None or node.text is None:
        raise CurrencyApiError(f"В XML нет поля {tag}.")
    return node.text.strip()


def _parse_float(value: str) -> float:
    """Преобразовать число из формата ЦБ РФ в float."""
    return float(value.replace(",", "."))


def get_currencies(
    url: str = CBR_DAILY_URL,
    timeout: int = 10,
) -> list[Currency]:
    """Получить список валют с сайта ЦБ РФ."""
    try:
        with urlopen(url, timeout=timeout) as response:
            xml_data = response.read()
    except (OSError, URLError) as error:
        raise CurrencyApiError("Не удалось получить курсы валют.") from error

    try:
        root = ElementTree.fromstring(xml_data)
    except ElementTree.ParseError as error:
        raise CurrencyApiError("Сервис вернул некорректный XML.") from error

    currencies: list[Currency] = []
    for valute in root.findall("Valute"):
        currency = Currency(
            currency_id=valute.attrib.get("ID", ""),
            num_code=_text(valute, "NumCode"),
            char_code=_text(valute, "CharCode"),
            nominal=int(_text(valute, "Nominal")),
            name=_text(valute, "Name"),
            value=_parse_float(_text(valute, "Value")),
        )
        currencies.append(currency)

    if not currencies:
        raise CurrencyApiError("Список валют пустой.")

    return currencies

