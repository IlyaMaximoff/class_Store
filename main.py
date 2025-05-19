class Store():

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_product(self, product, price):
        self.items[product] = price

    def dell_product(self, product):
        if product in self.items:
            del self.items[product]
        else:
            print(f"Товар {product} не найден")

    def find_price(self, product):
        if product in self.items:
            pr = self.items.get(product)
            print(f"Цена {product}: {pr}")
        else:
            print(f"Товар {product} не найден")

    def new_price(self,product, price):
        if product in self.items:
            self.items.update({product:price})
            print(f"Новая цена на {product}: {price}")
        else:
            print(f"Товар {product} не найден")

    def info(self):
        print(f"Магазин:{self.name}, Адрес:{self.address}")
        print(f"{self.items}")

w = Store('Sevens', 'Moscow')
w.add_product('бананы',150)
w.add_product('яблоки',100)
w.add_product('арбузы',500)
w.info()
#w.dell_product('яблоки')
#w.info()
#w.find_price('арбуз')
#w.new_price('арбуз','800')
#w.info()
