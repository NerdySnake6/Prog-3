"""Запуск HTTPServer и маршрутизация запросов."""

from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from jinja2 import Environment, PackageLoader, select_autoescape

from myapp.controllers.authorController import show_author, show_index
from myapp.controllers.currenciesController import show_currencies
from myapp.controllers.data import MAIN_APP, NAVIGATION
from myapp.controllers.userController import show_user, show_users

HOST = "localhost"
PORT = 8000
STATIC_DIR = Path(__file__).parent / "static"

# Environment создается один раз, чтобы Jinja2 мог кэшировать шаблоны.
env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape(),
)


class AppRequestHandler(BaseHTTPRequestHandler):
    """Обработчик GET-запросов приложения."""

    def do_GET(self) -> None:
        """Обработать GET-запрос от браузера."""
        status, content_type, body = build_response(self.path)
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body)


def build_response(path: str) -> tuple[int, str, bytes]:
    """Построить ответ сервера по пути запроса."""
    parsed = urlparse(path)
    query = parse_qs(parsed.query)

    if parsed.path == "/static/style.css":
        return _static_response("style.css", "text/css; charset=utf-8")

    if parsed.path == "/":
        return _html_response(200, show_index(env))
    if parsed.path == "/author":
        return _html_response(200, show_author(env))
    if parsed.path == "/users":
        return _html_response(200, show_users(env))
    if parsed.path == "/user":
        status, html = show_user(env, query)
        return _html_response(status, html)
    if parsed.path == "/currencies":
        return _html_response(200, show_currencies(env))

    template = env.get_template("404.html")
    html = template.render(
        app=MAIN_APP,
        navigation=NAVIGATION,
        message="Страница не найдена.",
    )
    return _html_response(404, html)


def _html_response(status: int, html: str) -> tuple[int, str, bytes]:
    """Собрать HTML-ответ."""
    return status, "text/html; charset=utf-8", html.encode("utf-8")


def _static_response(
    file_name: str,
    content_type: str,
) -> tuple[int, str, bytes]:
    """Отдать статический файл."""
    file_path = STATIC_DIR / file_name
    if not file_path.exists():
        return 404, "text/plain; charset=utf-8", b"Not found"
    return 200, content_type, file_path.read_bytes()


def run_server() -> None:
    """Запустить локальный сервер."""
    server = HTTPServer((HOST, PORT), AppRequestHandler)
    print(f"Сервер запущен: http://{HOST}:{PORT}/")
    server.serve_forever()


if __name__ == "__main__":
    run_server()

