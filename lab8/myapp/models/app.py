"""Модель приложения."""

from myapp.models.author import Author


class App:
    """Хранит название, версию и автора приложения."""

    def __init__(self, name: str, version: str, author: Author) -> None:
        """Создать приложение."""
        self.name = name
        self.version = version
        self.author = author

    @property
    def name(self) -> str:
        """Вернуть название приложения."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Название приложения должно быть строкой.")
        if not value.strip():
            raise ValueError("Название приложения не может быть пустым.")
        self.__name = value.strip()

    @property
    def version(self) -> str:
        """Вернуть версию приложения."""
        return self.__version

    @version.setter
    def version(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Версия должна быть строкой.")
        if not value.strip():
            raise ValueError("Версия не может быть пустой.")
        self.__version = value.strip()

    @property
    def author(self) -> Author:
        """Вернуть автора приложения."""
        return self.__author

    @author.setter
    def author(self, value: Author) -> None:
        if not isinstance(value, Author):
            raise TypeError("Автор должен быть объектом Author.")
        self.__author = value

