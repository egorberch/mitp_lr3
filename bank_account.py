"""Задание №3 (средней сложности): Класс «Банковский счёт»."""


class BankAccount:
    """Банковский счёт с операциями пополнения и снятия."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self) -> float:
        """Текущий баланс счёта."""
        return self._balance

    def deposit(self, amount: float) -> float:
        """Пополнение счёта."""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Снятие средств со счёта."""
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счёте")
        self._balance -= amount
        return self._balance

    def __str__(self) -> str:
        return f"Счёт {self.owner}: {self._balance:.2f} руб."


def main() -> None:
    """Демонстрация работы класса BankAccount."""
    account = BankAccount("Егор", 1000.0)
    print(account)

    account.deposit(500.0)
    print(f"После пополнения: {account.balance:.2f} руб.")

    account.withdraw(300.0)
    print(f"После снятия: {account.balance:.2f} руб.")


if __name__ == "__main__":
    main()
