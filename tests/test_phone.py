import pytest
from src.item import Item
from src.phone import Phone


def test_init():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3
