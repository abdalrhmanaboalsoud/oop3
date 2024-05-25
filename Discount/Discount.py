from abc import ABC, abstractmethod
from enum import Enum

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, amount):
        pass

class NoDiscountStrategy(DiscountStrategy):
    def calculate_discount(self, amount):
        return amount

class FlatDiscountStrategy(DiscountStrategy):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def calculate_discount(self, amount):
        discount = amount * self.discount_percentage / 100
        return amount - discount

class SaleDiscountStrategy(DiscountStrategy):
    def __init__(self, sale_percentage):
        self.sale_percentage = sale_percentage

    def calculate_discount(self, amount):
        new_price = amount * (100 - self.sale_percentage) / 100
        return new_price

class DiscountType(Enum):
    NO_DISCOUNT = NoDiscountStrategy()
    FLAT_DISCOUNT = FlatDiscountStrategy(10)
    SALE_DISCOUNT = SaleDiscountStrategy(20)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_final_price(self, discount_strategy: DiscountStrategy):
        return discount_strategy.calculate_discount(self.price)

if __name__ == "__main__":
    product = Product("T-Shirt", 20)

    # No discount
    final_price = product.get_final_price(DiscountType.NO_DISCOUNT.value)
    print(f"Product: {product.name}, Price: ${final_price:.2f}")

    # Flat discount
    final_price = product.get_final_price(DiscountType.FLAT_DISCOUNT.value)
    print(f"Product: {product.name}, Price with 10% discount: ${final_price:.2f}")

    # Sale discount
    final_price = product.get_final_price(DiscountType.SALE_DISCOUNT.value)
    print(f"Product: {product.name}, Price with 20% sale: ${final_price:.2f}")
