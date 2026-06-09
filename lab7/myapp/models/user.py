"""Модель пользователя."""


class User:
    """Хранит пользователя приложения."""

    def __init__(self, user_id: int, name: str) -> None:
        """Создать пользователя с id и именем."""
        self.id = user_id
        self.name = name

    @property
    def id(self) -> int:
        """Вернуть id пользователя."""
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Id пользователя должен быть числом.")
        if value <= 0:
            raise ValueError("Id пользователя должен быть больше нуля.")
        self._id = value

    @property
    def name(self) -> str:
        """Вернуть имя пользователя."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Имя пользователя должно быть строкой.")
        if not value.strip():
            raise ValueError("Имя пользователя не может быть пустым.")
        self._name = value.strip()

