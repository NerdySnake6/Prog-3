"""Модель пользователя."""


class User:
    """Хранит пользователя приложения."""

    def __init__(self, name: str, user_id: int | None = None) -> None:
        """Создать пользователя."""
        self.id = user_id
        self.name = name

    @property
    def id(self) -> int | None:
        """Вернуть id пользователя."""
        return self.__id

    @id.setter
    def id(self, value: int | None) -> None:
        if value is not None and not isinstance(value, int):
            raise TypeError("Id пользователя должен быть числом.")
        if isinstance(value, int) and value <= 0:
            raise ValueError("Id пользователя должен быть больше нуля.")
        self.__id = value

    @property
    def name(self) -> str:
        """Вернуть имя пользователя."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Имя пользователя должно быть строкой.")
        if not value.strip():
            raise ValueError("Имя пользователя не может быть пустым.")
        self.__name = value.strip()

