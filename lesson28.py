# OOP
from abc import ABC, abstractmethod

class Product(ABC):
    total_products = 0

    def __init__(self, name, year, price, quantity, date):
        self.name = name
        self.year = year
        self.price = price
        self.quantity = quantity
        self.date = date
        Product.total_products += 1

    @classmethod
    def get_total_products(cls):
        return Product.total_products

    def display_info(self):
        return f'{self.name}, {self.year}, {self.price}, {self.quantity}, {self.date}'


class FoodItem(Product):
    expiry_date = None

    def __init__(self, name, year, price, quantity, date):
        super().__init__(name, year, price, quantity, date)
        self.expiry_date = date

    def display_info(self):
        return f'{self.name}, {self.year}, {self.price}, {self.quantity}, {self.date}, Yaroqlilik muddati: {self.expiry_date}'


class ElectronicItem(Product):
    warranty_years = None

    def __init__(self, name, year, price, quantity, date):
        super().__init__(name, year, price, quantity, date)
        self.warranty_years = year

    def display_info(self):
        return f"{self.name}, {self.year}, {self.price}, {self.quantity}, {self.date}, Warranty years: {self.warranty_years}"


class Warehouse:
    total_warehouses = 0

    def __init__(self, name):
        self.name = name
        self.products = {}
        Warehouse.total_warehouses += 1

    def add_product(self, product):
        if isinstance(product, Product):
            self.products[product.name] = product
        else:
            raise TypeError ("Faqat Product obyektlarini qo'shish mumkin")
    def list_products(self):
        for product in self.products.values():
            print(product.display_info())

