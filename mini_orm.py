"""Задание №7 (повышенной сложности): Мини-ORM: класс «Таблица», методы insert, select."""

from typing import Any


class Table:
    """Таблица в памяти с поддержкой insert и select."""

    def __init__(self, name: str, schema: dict[str, type[Any]]) -> None:
        self.name = name
        self.schema = schema
        self._rows: list[dict[str, Any]] = []
        self._next_id = 1

    def insert(self, **kwargs: Any) -> dict[str, Any]:
        """Добавляет запись в таблицу с проверкой типов по схеме."""
        for field, field_type in self.schema.items():
            if field not in kwargs:
                raise ValueError(f"Пропущено поле '{field}'")
            if not isinstance(kwargs[field], field_type):
                raise TypeError(
                    f"Поле '{field}' должно быть типа {field_type.__name__}"
                )

        row = {"id": self._next_id, **kwargs}
        self._rows.append(row)
        self._next_id += 1
        return row

    def select(self, **filters: Any) -> list[dict[str, Any]]:
        """Возвращает записи, подходящие под условия фильтрации."""
        if not filters:
            return list(self._rows)

        result = []
        for row in self._rows:
            if all(row.get(k) == v for k, v in filters.items()):
                result.append(row)
        return result


def main() -> None:
    """Демонстрация работы класса Table."""
    users = Table("users", {"name": str, "age": int})

    users.insert(name="Егор", age=20)
    users.insert(name="Иван", age=19)
    users.insert(name="Анна", age=20)

    print("Все записи:", users.select())
    print("Возраст 20:", users.select(age=20))


if __name__ == "__main__":
    main()
