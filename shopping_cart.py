"""shopping_cart.py

Simple shopping cart module for the portfolio.
Provides a minimal ShoppingCart class with add/remove/total and a small demo when run as __main__.
"""

from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Item:
    name: str
    price: float
    qty: int = 1

@dataclass
class ShoppingCart:
    items: Dict[str, Item] = field(default_factory=dict)

    def add_item(self, name: str, price: float, qty: int = 1) -> None:
        if name in self.items:
            self.items[name].qty += qty
        else:
            self.items[name] = Item(name, price, qty)

    def remove_item(self, name: str, qty: int = 1) -> None:
        if name not in self.items:
            raise KeyError(f"Item {name!r} not in cart")
        self.items[name].qty -= qty
        if self.items[name].qty <= 0:
            del self.items[name]

    def total(self) -> float:
        return round(sum(item.price * item.qty for item in self.items.values()), 2)

    def apply_discount(self, percent: float) -> float:
        """Apply a percentage discount (0-100) and return discounted total."""
        assert 0 <= percent <= 100
        return round(self.total() * (1 - percent / 100.0), 2)

    def __repr__(self) -> str:
        lines = [f"{it.qty} × {it.name} @ {it.price} = {it.qty * it.price}" for it in self.items.values()]
        return "\n".join(lines) or "(empty)"


if __name__ == "__main__":
    # Small demo
    cart = ShoppingCart()
    cart.add_item("T-shirt", 19.99, 2)
    cart.add_item("Mug", 7.5)
    print("Cart contents:\n", cart)
    print("Total:", cart.total())
    print("Total after 10% discount:", cart.apply_discount(10))
