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

mag1 = Store('Sevens', 'Moscow')
mag1.add_product('бананы',150)
mag1.add_product('яблоки',100)
mag1.add_product('арбузы',500)
mag1.info()
#mag1.dell_product('яблоки')
#mag1.info()
#mag1.find_price('арбуз')
#mag1.new_price('арбуз','800')
#mag1.info()

mag2 = Store('Eleven', 'Piter')
mag2.add_product('манго',650)
mag2.add_product('груши',300)
mag2.add_product('клубника',1000)
mag2.info()
#mag2.dell_product('яблоки')
#mag2.info()
#mag2.find_price('арбуз')
#mag2.new_price('арбуз','800')
#mag2.info()

mag3 = Store('Monetka', 'Novosibirsk')
mag3.add_product('картофель',100)
mag3.add_product('морковь',80)
mag3.add_product('капуста',50)
mag3.info()
#mag3.dell_product('яблоки')
#mag3.info()
#mag3.find_price('арбуз')
#mag3.new_price('арбуз','800')
#mag3.info()
