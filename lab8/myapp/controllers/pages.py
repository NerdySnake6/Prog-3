"""Контроллер для рендеринга HTML-страниц."""

from jinja2 import Environment

from myapp.controllers.authorController import MAIN_APP, MAIN_AUTHOR, NAVIGATION
from myapp.controllers.currenciesController import CurrenciesController
from myapp.controllers.userController import UserController


class PagesController:
    """Рендерит страницы через Jinja2."""

    def __init__(
        self,
        env: Environment,
        currencies: CurrenciesController,
        users: UserController,
    ) -> None:
        """Создать контроллер страниц."""
        self.env = env
        self.currencies = currencies
        self.users = users

    def index(self) -> str:
        """Сформировать главную страницу."""
        template = self.env.get_template("index.html")
        return template.render(
            app=MAIN_APP,
            author=MAIN_AUTHOR,
            navigation=NAVIGATION,
        )

    def author(self) -> str:
        """Сформировать страницу автора."""
        template = self.env.get_template("author.html")
        return template.render(
            app=MAIN_APP,
            author=MAIN_AUTHOR,
            navigation=NAVIGATION,
        )

    def users_page(self) -> str:
        """Сформировать страницу пользователей."""
        template = self.env.get_template("users.html")
        return template.render(
            app=MAIN_APP,
            navigation=NAVIGATION,
            users=self.users.list_users(),
        )

    def user_page(self, user_id: int) -> tuple[int, str]:
        """Сформировать страницу одного пользователя."""
        user = self.users.get_user(user_id)
        if user is None:
            return 404, self.not_found("Пользователь не найден.")

        template = self.env.get_template("user.html")
        html = template.render(
            app=MAIN_APP,
            navigation=NAVIGATION,
            user=user,
            currencies=self.users.get_user_currencies(user_id),
        )
        return 200, html

    def currencies_page(self, message: str = "") -> str:
        """Сформировать страницу валют."""
        template = self.env.get_template("currencies.html")
        return template.render(
            app=MAIN_APP,
            navigation=NAVIGATION,
            currencies=self.currencies.list_currencies(),
            message=message,
        )

    def not_found(self, message: str) -> str:
        """Сформировать страницу ошибки 404."""
        template = self.env.get_template("404.html")
        return template.render(
            app=MAIN_APP,
            navigation=NAVIGATION,
            message=message,
        )

