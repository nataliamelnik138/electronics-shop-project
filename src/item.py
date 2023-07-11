import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл поврежден'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        cls.all = []
        if not os.path.exists('../src/items.csv'):
            raise FileNotFoundError("Отсутствует файл item.csv")
        with open('../src/items.csv', 'rt', encoding='utf-8') as csvfile:
            data = csv.DictReader(csvfile, delimiter=',')
            key_data = data.fieldnames
            if key_data != ['name', "price", "quantity"]:
                raise InstantiateCSVError("Файл item.csv поврежден")
            for line in data:
                cls(line['name'], float(line["price"]), cls.string_to_number(line["quantity"]))

    @staticmethod
    def string_to_number(number_str):
        """Возвращает число из числа-строки"""
        return int(float(number_str))

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError('Складывать можно только экземпляры классов Phone или Item')
