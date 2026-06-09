"""Модель валюты."""


class Currency:
    """Хранит данные валюты."""

    def __init__(
        self,
        num_code: str,
        char_code: str,
        name: str,
        value: float,
        nominal: int,
        currency_id: int | None = None,
    ) -> None:
        """Создать валюту."""
        self.id = currency_id
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value
        self.nominal = nominal

    @property
    def id(self) -> int | None:
        """Вернуть id валюты."""
        return self.__id

    @id.setter
    def id(self, value: int | None) -> None:
        if value is not None and not isinstance(value, int):
            raise TypeError("Id валюты должен быть числом.")
        if isinstance(value, int) and value <= 0:
            raise ValueError("Id валюты должен быть больше нуля.")
        self.__id = value

    @property
    def num_code(self) -> str:
        """Вернуть цифровой код валюты."""
        return self.__num_code

    @num_code.setter
    def num_code(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Цифровой код должен быть строкой.")
        if not value.strip():
            raise ValueError("Цифровой код не может быть пустым.")
        self.__num_code = value.strip()

    @property
    def char_code(self) -> str:
        """Вернуть буквенный код валюты."""
        return self.__char_code

    @char_code.setter
    def char_code(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Код валюты должен быть строкой.")
        value = value.strip().upper()
        if len(value) != 3:
            raise ValueError("Код валюты должен состоять из 3 символов.")
        self.__char_code = value

    @property
    def name(self) -> str:
        """Вернуть название валюты."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Название валюты должно быть строкой.")
        if not value.strip():
            raise ValueError("Название валюты не может быть пустым.")
        self.__name = value.strip()

    @property
    def value(self) -> float:
        """Вернуть курс валюты."""
        return self.__value

    @value.setter
    def value(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Курс валюты должен быть числом.")
        if value < 0:
            raise ValueError("Курс валюты не может быть отрицательным.")
        self.__value = float(value)

    @property
    def nominal(self) -> int:
        """Вернуть номинал валюты."""
        return self.__nominal

    @nominal.setter
    def nominal(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Номинал должен быть числом.")
        if value <= 0:
            raise ValueError("Номинал должен быть больше нуля.")
        self.__nominal = value

    def to_dict(self) -> dict[str, int | str | float | None]:
        """Преобразовать валюту в словарь для шаблона."""
        return {
            "id": self.id,
            "num_code": self.num_code,
            "char_code": self.char_code,
            "name": self.name,
            "value": self.value,
            "nominal": self.nominal,
        }

