"""Контроллер для работы с SQLite в памяти."""

import sqlite3

from myapp.models import Currency, User


class CurrencyRatesCRUD:
    """Выполняет CRUD-операции для учебной базы валют."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        """Сохранить подключение к базе данных."""
        self.connection = connection
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")

    def create_tables(self) -> None:
        """Создать таблицы user, currency и user_currency."""
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS currency (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                num_code TEXT NOT NULL,
                char_code TEXT NOT NULL,
                name TEXT NOT NULL,
                value FLOAT,
                nominal INTEGER
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_currency (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                currency_id INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES user(id),
                FOREIGN KEY(currency_id) REFERENCES currency(id)
            )
            """
        )
        self.connection.commit()

    def seed_data(self) -> None:
        """Заполнить базу начальными учебными данными."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) AS count FROM currency")
        if cursor.fetchone()["count"] > 0:
            return

        users = [{"name": "Иван"}, {"name": "Анна"}, {"name": "Мария"}]
        currencies = [
            {
                "num_code": "840",
                "char_code": "USD",
                "name": "Доллар США",
                "value": 90.0,
                "nominal": 1,
            },
            {
                "num_code": "978",
                "char_code": "EUR",
                "name": "Евро",
                "value": 91.0,
                "nominal": 1,
            },
            {
                "num_code": "156",
                "char_code": "CNY",
                "name": "Китайский юань",
                "value": 12.5,
                "nominal": 1,
            },
        ]

        # Здесь используются именованные параметры, а не склейка строк.
        cursor.executemany("INSERT INTO user(name) VALUES(:name)", users)
        cursor.executemany(
            """
            INSERT INTO currency(num_code, char_code, name, value, nominal)
            VALUES(:num_code, :char_code, :name, :value, :nominal)
            """,
            currencies,
        )
        cursor.executemany(
            """
            INSERT INTO user_currency(user_id, currency_id)
            VALUES(:user_id, :currency_id)
            """,
            [
                {"user_id": 1, "currency_id": 1},
                {"user_id": 1, "currency_id": 2},
                {"user_id": 2, "currency_id": 3},
            ],
        )
        self.connection.commit()

    def _create(self, currency: Currency) -> int:
        """Добавить валюту и вернуть ее id."""
        cursor = self.connection.cursor()
        cursor.execute(
            """
            INSERT INTO currency(num_code, char_code, name, value, nominal)
            VALUES(?, ?, ?, ?, ?)
            """,
            (
                currency.num_code,
                currency.char_code,
                currency.name,
                currency.value,
                currency.nominal,
            ),
        )
        self.connection.commit()
        return int(cursor.lastrowid)

    def _read(self) -> list[dict[str, int | str | float]]:
        """Вернуть все валюты."""
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT id, num_code, char_code, name, value, nominal
            FROM currency
            ORDER BY id
            """
        )
        return [dict(row) for row in cursor.fetchall()]

    def _update(self, values: dict[str, float]) -> int:
        """Обновить курс валют по их буквенным кодам."""
        cursor = self.connection.cursor()
        updated = 0

        for char_code, value in values.items():
            cursor.execute(
                "UPDATE currency SET value = ? WHERE char_code = ?",
                (float(value), char_code.upper()),
            )
            updated += cursor.rowcount

        self.connection.commit()
        return updated

    def _delete(self, currency_id: int) -> bool:
        """Удалить валюту по id."""
        cursor = self.connection.cursor()
        cursor.execute(
            "DELETE FROM user_currency WHERE currency_id = ?",
            (currency_id,),
        )
        cursor.execute("DELETE FROM currency WHERE id = ?", (currency_id,))
        self.connection.commit()
        return cursor.rowcount > 0

    def get_currency_by_char_code(
        self,
        char_code: str,
    ) -> dict[str, int | str | float] | None:
        """Найти валюту по буквенному коду."""
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT id, num_code, char_code, name, value, nominal
            FROM currency
            WHERE char_code = ?
            """,
            (char_code.upper(),),
        )
        row = cursor.fetchone()
        if row is None:
            return None
        return dict(row)

    def list_users(self) -> list[dict[str, int | str]]:
        """Вернуть список пользователей."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name FROM user ORDER BY id")
        return [dict(row) for row in cursor.fetchall()]

    def get_user(self, user_id: int) -> User | None:
        """Найти пользователя по id."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name FROM user WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if row is None:
            return None
        return User(user_id=int(row["id"]), name=str(row["name"]))

    def get_user_currencies(
        self,
        user_id: int,
    ) -> list[dict[str, int | str | float]]:
        """Вернуть валюты, на которые подписан пользователь."""
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT c.id, c.num_code, c.char_code, c.name, c.value, c.nominal
            FROM currency AS c
            JOIN user_currency AS uc ON uc.currency_id = c.id
            WHERE uc.user_id = ?
            ORDER BY c.char_code
            """,
            (user_id,),
        )
        return [dict(row) for row in cursor.fetchall()]
