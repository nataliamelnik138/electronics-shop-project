import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200_000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_name():
    """Тестирует применение декоратора @property к приватному агрументу name"""
    item = Item("Телефон", 10000, 20)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    # Если файл поврежден
    # with pytest.raises(InstantiateCSVError, match='Файл item.csv поврежден'):
    #     Item.instantiate_from_csv()

    # Если файл отсутствует
    # with pytest.raises(FileNotFoundError, match='Файл item.csv поврежден'):
#     Item.instantiate_from_csv()


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Телефон", 20000, 10)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert item1 + item2 == 30
    assert phone1 + phone1 == 10
    with pytest.raises(TypeError, match='Складывать можно только экземпляры классов Phone или Item'):
        phone1 + 10
