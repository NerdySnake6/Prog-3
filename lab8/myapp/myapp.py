"""Запуск HTTPServer и простого GET-роутера."""

import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse

from jinja2 import Environment, PackageLoader, select_autoescape

from myapp.controllers.currenciesController import CurrenciesController
from myapp.controllers.databaseController import CurrencyRatesCRUD
from myapp.controllers.pages import PagesController
from myapp.controllers.userController import UserController

HOST = "localhost"
PORT = 8001
STATIC_DIR = Path(__file__).parent / "static"

env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape(),
)


class Router:
    """Обрабатывает GET-маршруты приложения."""

    def __init__(
        self,
        pages: PagesController,
        currencies: CurrenciesController,
    ) -> None:
        """Создать роутер."""
        self.pages = pages
        self.currencies = currencies

    def handle(self, path: str) -> tuple[int, dict[str, str], bytes]:
        """Вернуть ответ для указанного пути."""
        parsed = urlparse(path)
        query = parse_qs(parsed.query)

        if parsed.path == "/static/style.css":
            return self._static("style.css", "text/css; charset=utf-8")
        if parsed.path == "/":
            return self._html(200, self.pages.index())
        if parsed.path == "/author":
            return self._html(200, self.pages.author())
        if parsed.path == "/users":
            return self._html(200, self.pages.users_page())
        if parsed.path == "/user":
            user_id = self._int_arg(query, "id")
            status, html = self.pages.user_page(user_id)
            return self._html(status, html)
        if parsed.path == "/currencies":
            message = query.get("message", [""])[0]
            return self._html(200, self.pages.currencies_page(message))
        if parsed.path == "/currency/create":
            return self._create_currency(query)
        if parsed.path == "/currency/update":
            return self._update_currency(query)
        if parsed.path == "/currency/delete":
            return self._delete_currency(query)
        if parsed.path == "/currency/show":
            self.currencies.show_currencies()
            return self._redirect("Валюты выведены в консоль.")

        return self._html(404, self.pages.not_found("Страница не найдена."))

    def _create_currency(
        self,
        query: dict[str, list[str]],
    ) -> tuple[int, dict[str, str], bytes]:
        """Обработать добавление валюты."""
        try:
            self.currencies.create_currency(
                num_code=query["num_code"][0],
                char_code=query["char_code"][0],
                name=query["name"][0],
                value=float(query["value"][0]),
                nominal=int(query["nominal"][0]),
            )
            return self._redirect("Валюта добавлена.")
        except (KeyError, ValueError, TypeError):
            return self._redirect("Не получилось добавить валюту.")

    def _update_currency(
        self,
        query: dict[str, list[str]],
    ) -> tuple[int, dict[str, str], bytes]:
        """Обработать обновление курса."""
        try:
            char_code, values = next(iter(query.items()))
            updated = self.currencies.update_currency(char_code, float(values[0]))
        except (StopIteration, ValueError):
            return self._redirect("Не получилось обновить курс.")

        if updated:
            return self._redirect("Курс обновлен.")
        return self._redirect("Валюта не найдена.")

    def _delete_currency(
        self,
        query: dict[str, list[str]],
    ) -> tuple[int, dict[str, str], bytes]:
        """Обработать удаление валюты."""
        currency_id = self._int_arg(query, "id")
        if self.currencies.delete_currency(currency_id):
            return self._redirect("Валюта удалена.")
        return self._redirect("Валюта не найдена.")

    def _redirect(self, message: str) -> tuple[int, dict[str, str], bytes]:
        """Сделать редирект на страницу валют."""
        params = urlencode({"message": message})
        return 302, {"Location": f"/currencies?{params}"}, b""

    def _html(
        self,
        status: int,
        html: str,
    ) -> tuple[int, dict[str, str], bytes]:
        """Собрать HTML-ответ."""
        return status, {"Content-Type": "text/html; charset=utf-8"}, html.encode()

    def _static(
        self,
        file_name: str,
        content_type: str,
    ) -> tuple[int, dict[str, str], bytes]:
        """Вернуть статический файл."""
        file_path = STATIC_DIR / file_name
        if not file_path.exists():
            return 404, {"Content-Type": "text/plain; charset=utf-8"}, b""
        return 200, {"Content-Type": content_type}, file_path.read_bytes()

    def _int_arg(self, query: dict[str, list[str]], name: str) -> int:
        """Получить числовой query-параметр."""
        try:
            return int(query.get(name, ["0"])[0])
        except ValueError:
            return 0


class AppRequestHandler(BaseHTTPRequestHandler):
    """Обработчик HTTP-запросов."""

    def do_GET(self) -> None:
        """Обработать GET-запрос."""
        status, headers, body = router.handle(self.path)
        self.send_response(status)
        for name, value in headers.items():
            self.send_header(name, value)
        self.end_headers()
        self.wfile.write(body)


def create_router() -> Router:
    """Создать роутер с новой базой данных в памяти."""
    connection = sqlite3.connect(":memory:", check_same_thread=False)
    db_controller = CurrencyRatesCRUD(connection)
    db_controller.create_tables()
    db_controller.seed_data()
    currencies = CurrenciesController(db_controller)
    users = UserController(db_controller)
    pages = PagesController(env, currencies, users)
    return Router(pages, currencies)


def run_server() -> None:
    """Запустить локальный сервер."""
    server = HTTPServer((HOST, PORT), AppRequestHandler)
    print(f"Сервер запущен: http://{HOST}:{PORT}/")
    server.serve_forever()


router = create_router()

if __name__ == "__main__":
    run_server()

