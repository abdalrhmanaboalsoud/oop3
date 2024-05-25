import pytest
from Discount.Discount import*

def test_no_discount_strategy():
    product = Product("T-Shirt", 20)
    discount_strategy = NoDiscountStrategy()
    assert product.get_final_price(discount_strategy) == 20

def test_flat_discount_strategy():
    product = Product("T-Shirt", 20)
    discount_strategy = FlatDiscountStrategy(10)
    assert product.get_final_price(discount_strategy) == 18

def test_sale_discount_strategy():
    product = Product("T-Shirt", 20)
    discount_strategy = SaleDiscountStrategy(20)
    assert product.get_final_price(discount_strategy) == 16

def test_flat_discount_strategy_with_different_percentage():
    product = Product("T-Shirt", 50)
    discount_strategy = FlatDiscountStrategy(25)
    assert product.get_final_price(discount_strategy) == 37.5

def test_sale_discount_strategy_with_different_percentage():
    product = Product("T-Shirt", 50)
    discount_strategy = SaleDiscountStrategy(50)
    assert product.get_final_price(discount_strategy) == 25

