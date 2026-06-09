"""Контроллер пользователей."""

from myapp.controllers.databaseController import CurrencyRatesCRUD
from myapp.models import User


class UserController:
    """Получает пользователей и их подписки из базы."""

    def __init__(self, db_controller: CurrencyRatesCRUD) -> None:
        """Создать контроллер пользователей."""
        self.db = db_controller

    def list_users(self) -> list[dict[str, int | str]]:
        """Вернуть список пользователей."""
        return self.db.list_users()

    def get_user(self, user_id: int) -> User | None:
        """Вернуть пользователя по id."""
        return self.db.get_user(user_id)

    def get_user_currencies(
        self,
        user_id: int,
    ) -> list[dict[str, int | str | float]]:
        """Вернуть валюты пользователя."""
        return self.db.get_user_currencies(user_id)

