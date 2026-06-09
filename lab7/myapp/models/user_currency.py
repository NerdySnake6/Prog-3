"""Модель связи пользователя и валюты."""


class UserCurrency:
    """Хранит подписку пользователя на валюту."""

    def __init__(
        self,
        relation_id: int,
        user_id: int,
        currency_id: str,
    ) -> None:
        """Создать связь между пользователем и валютой."""
        self.id = relation_id
        self.user_id = user_id
        self.currency_id = currency_id

    @property
    def id(self) -> int:
        """Вернуть id связи."""
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Id связи должен быть числом.")
        if value <= 0:
            raise ValueError("Id связи должен быть больше нуля.")
        self._id = value

    @property
    def user_id(self) -> int:
        """Вернуть id пользователя."""
        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Id пользователя должен быть числом.")
        if value <= 0:
            raise ValueError("Id пользователя должен быть больше нуля.")
        self._user_id = value

    @property
    def currency_id(self) -> str:
        """Вернуть id валюты."""
        return self._currency_id

    @currency_id.setter
    def currency_id(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Id валюты должен быть строкой.")
        if not value.strip():
            raise ValueError("Id валюты не может быть пустым.")
        self._currency_id = value.strip()

