"""Задание №5 (средней сложности): Наследование: «Животное» -> «Собака»."""


class Animal:
    """Базовый класс животного."""

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        """Возвращает звук, который издаёт животное."""
        return f"{self.name} издаёт звук"


class Dog(Animal):
    """Класс собаки, наследуемый от Animal."""

    def __init__(self, name: str, breed: str = "Дворняжка") -> None:
        super().__init__(name)
        self.breed = breed

    def speak(self) -> str:
        """Переопределённый метод подачи голоса."""
        return f"{self.name} говорит Гав!"


def main() -> None:
    """Демонстрация работы классов Animal и Dog."""
    animal = Animal("Зверь")
    dog = Dog("Шарик", "Овчарка")

    print(animal.speak())
    print(f"{dog.name} ({dog.breed}): {dog.speak()}")


if __name__ == "__main__":
    main()
