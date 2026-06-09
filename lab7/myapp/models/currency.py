"""Модель валюты."""


class Currency:
    """Хранит данные одной валюты."""

    def __init__(
        self,
        currency_id: str,
        num_code: str,
        char_code: str,
        name: str,
        value: float,
        nominal: int,
    ) -> None:
        """Создать валюту с основными данными."""
        self.id = currency_id
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value
        self.nominal = nominal

    @property
    def id(self) -> str:
        """Вернуть id валюты."""
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Id валюты должен быть строкой.")
        if not value.strip():
            raise ValueError("Id валюты не может быть пустым.")
        self._id = value.strip()

    @property
    def num_code(self) -> str:
        """Вернуть цифровой код валюты."""
        return self._num_code

    @num_code.setter
    def num_code(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Цифровой код должен быть строкой.")
        if not value.strip():
            raise ValueError("Цифровой код не может быть пустым.")
        self._num_code = value.strip()

    @property
    def char_code(self) -> str:
        """Вернуть буквенный код валюты."""
        return self._char_code

    @char_code.setter
    def char_code(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Буквенный код должен быть строкой.")
        if not value.strip():
            raise ValueError("Буквенный код не может быть пустым.")
        self._char_code = value.strip().upper()

    @property
    def name(self) -> str:
        """Вернуть название валюты."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Название валюты должно быть строкой.")
        if not value.strip():
            raise ValueError("Название валюты не может быть пустым.")
        self._name = value.strip()

    @property
    def value(self) -> float:
        """Вернуть курс валюты."""
        return self._value

    @value.setter
    def value(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Курс валюты должен быть числом.")
        if value <= 0:
            raise ValueError("Курс валюты должен быть больше нуля.")
        self._value = float(value)

    @property
    def nominal(self) -> int:
        """Вернуть номинал валюты."""
        return self._nominal

    @nominal.setter
    def nominal(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Номинал должен быть числом.")
        if value <= 0:
            raise ValueError("Номинал должен быть больше нуля.")
        self._nominal = value

