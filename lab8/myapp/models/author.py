"""Модель автора приложения."""


class Author:
    """Хранит имя автора и учебную группу."""

    def __init__(self, name: str, group: str) -> None:
        """Создать автора."""
        self.name = name
        self.group = group

    @property
    def name(self) -> str:
        """Вернуть имя автора."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Имя автора должно быть строкой.")
        if not value.strip():
            raise ValueError("Имя автора не может быть пустым.")
        self.__name = value.strip()

    @property
    def group(self) -> str:
        """Вернуть учебную группу."""
        return self.__group

    @group.setter
    def group(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Группа должна быть строкой.")
        if not value.strip():
            raise ValueError("Группа не может быть пустой.")
        self.__group = value.strip()

