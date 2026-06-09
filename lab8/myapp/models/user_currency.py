"""Модель связи пользователя и валюты."""


class UserCurrency:
    """Хранит подписку пользователя на валюту."""

    def __init__(
        self,
        user_id: int,
        currency_id: int,
        relation_id: int | None = None,
    ) -> None:
        """Создать связь пользователя и валюты."""
        self.id = relation_id
        self.user_id = user_id
        self.currency_id = currency_id

    @property
    def id(self) -> int | None:
        """Вернуть id связи."""
        return self.__id

    @id.setter
    def id(self, value: int | None) -> None:
        if value is not None and not isinstance(value, int):
            raise TypeError("Id связи должен быть числом.")
        if isinstance(value, int) and value <= 0:
            raise ValueError("Id связи должен быть больше нуля.")
        self.__id = value

    @property
    def user_id(self) -> int:
        """Вернуть id пользователя."""
        return self.__user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Id пользователя должен быть числом.")
        if value <= 0:
            raise ValueError("Id пользователя должен быть больше нуля.")
        self.__user_id = value

    @property
    def currency_id(self) -> int:
        """Вернуть id валюты."""
        return self.__currency_id

    @currency_id.setter
    def currency_id(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Id валюты должен быть числом.")
        if value <= 0:
            raise ValueError("Id валюты должен быть больше нуля.")
        self.__currency_id = value

