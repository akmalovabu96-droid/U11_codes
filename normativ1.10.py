# Computer va Meros olish
from abc import ABC, abstractmethod

class Computer(ABC):
    total_computers = 0

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        Computer.total_computers += 1

    @abstractmethod
    def display_info(self):
        return f'{self.brand} {self.model} {self.year} {self.price}'

    @classmethod
    def get_total_computers(cls):
        return Computer.total_computers

class Monoblock(Computer):
    def __init__(self, brand, model, year, price, screen_size):
        super().__init__(brand, model, year, price)
        self.screen_size = screen_size

    def display_info(self):
        return (f"Monoblock: {self.brand} {self.model}, "
                f"Yili: {self.year} "
                f"Narxi: {self.price} "
                f"Ekran o'lchami: {self.screen_size}")

class Notebook(Computer):
    def __init__(self, brand, model, year, price, battery_life):
        super().__init__(brand, model, year, price)
        self.battery_life = battery_life

    def display_info(self):
        return (f"Notebook: {self.brand} {self.model}, "
                f"Yili: {self.year}, "
                f"Narxi: {self.price}, "
                f"Batareya muddati: {self.battery_life} soat")

# Amaliyotda sinab ko'rish

# Ikki voris klassga obyektlar
obyektmono = Monoblock("Apple", "iMac", 1995, 1.299, 23.5)
obyektnote = Notebook("Dell", "XPS 13", 2015, 1.049, 18)
# Har birining ma'lumotini chiqaramiz
print(obyektmono.display_info())
print(obyektnote.display_info())

print("Jami kompyuterlar soni:", Computer.get_total_computers())
