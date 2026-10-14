"""Задание №3 (повышенной сложности): Система заказов («Товар», «Корзина»)."""


class Product:
    """Товар с названием и ценой."""

    def __init__(self, name: str, price: float) -> None:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.name = name
        self.price = float(price)

    def __repr__(self) -> str:
        return f"Product(name='{self.name}', price={self.price})"


class Cart:
    """Корзина покупателя."""

    def __init__(self) -> None:
        self._items: dict[str, tuple[Product, int]] = {}

    def add_product(self, product: Product, quantity: int = 1) -> None:
        """Добавляет товар в корзину."""
        if quantity <= 0:
            raise ValueError("Количество должно быть больше нуля")

        if product.name in self._items:
            current_product, current_qty = self._items[product.name]
            self._items[product.name] = (
                current_product,
                current_qty + quantity,
            )
        else:
            self._items[product.name] = (product, quantity)

    def remove_product(self, product_name: str) -> None:
        """Удаляет товар из корзины по названию."""
        if product_name not in self._items:
            raise KeyError(f"Товар '{product_name}' не найден в корзине")
        del self._items[product_name]

    def total_price(self) -> float:
        """Считает итоговую стоимость корзины."""
        return sum(
            product.price * qty for product, qty in self._items.values()
        )

    def get_items(self) -> list[str]:
        """Возвращает список позиций в текстовом виде."""
        result: list[str] = []
        for product, qty in self._items.values():
            cost = product.price * qty
            result.append(f"{product.name} x{qty} = {cost:.2f} руб.")
        return result


class Order:
    """Оформленный заказ на основе корзины."""

    def __init__(self, customer: str, cart: Cart) -> None:
        self.customer = customer
        self.items = cart.get_items()
        self.total = cart.total_price()

    def __str__(self) -> str:
        items_str = "\n  ".join(self.items)
        return (
            f"Заказ для: {self.customer}\n"
            f"  {items_str}\n"
            f"Итого: {self.total:.2f} руб."
        )


def main() -> None:
    """Демонстрация работы классов Product, Cart и Order."""
    laptop = Product("Ноутбук", 65000)
    mouse = Product("Мышь", 1500)

    cart = Cart()
    cart.add_product(laptop, 1)
    cart.add_product(mouse, 2)

    order = Order("Егор", cart)
    print(order)


if __name__ == "__main__":
    main()
