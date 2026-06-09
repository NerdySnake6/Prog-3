"""Модель автора приложения."""


class Author:
    """Хранит информацию об авторе лабораторной работы."""

    def __init__(self, name: str, group: str) -> None:
        """Создать автора с именем и группой."""
        self.name = name
        self.group = group

    @property
    def name(self) -> str:
        """Вернуть имя автора."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Имя автора должно быть строкой.")
        if not value.strip():
            raise ValueError("Имя автора не может быть пустым.")
        self._name = value.strip()

    @property
    def group(self) -> str:
        """Вернуть учебную группу автора."""
        return self._group

    @group.setter
    def group(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Группа должна быть строкой.")
        if not value.strip():
            raise ValueError("Группа не может быть пустой.")
        self._group = value.strip()

