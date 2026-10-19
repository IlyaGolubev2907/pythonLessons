class Flower:

    def __init__(self, name, price, lifetime):
        self.name = name
        self.price = price
        self.lifetime = lifetime


class Rose(Flower):
    def __init__(self):
        super().__init__("Роза", 250, 7)


class Tulip(Flower):
    def __init__(self):
        super().__init__("Тюльпан", 150, 5)


class Lily(Flower):
    def __init__(self):
        super().__init__("Лилия", 100, 8)


class Bouquet:

    def __init__(self):
        self.flowers = []
        self.accessories = []

    def get_total_price(self):
        price = 0
        for flower in self.flowers:
            price += flower.price
        for accessory in self.accessories:
            price += accessory.price
        return price

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def get_lifetime(self):

        if not self.flowers:
            return 0

        lifetime = 0
        for flower in self.flowers:
            lifetime += flower.lifetime

        return round(lifetime / len(self.flowers), 2)

    def price_sort(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def check_flower(self, name):
        for flower in self.flowers:
            if flower.name == name:
                return True
        return False


class Accessories:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Wrap(Accessories):
    def __init__(self):
        super().__init__("Обертка", 50)


class Tape(Accessories):
    def __init__(self):
        super().__init__("Лента", 25)


bouquet1 = Bouquet()

rose = Rose()
tulip = Tulip()
lily = Lily()

bouquet1.add_flower(rose)
bouquet1.add_flower(tulip)
bouquet1.add_flower(lily)

wrap = Wrap()
tape = Tape()

bouquet1.add_accessory(wrap)
bouquet1.add_accessory(tape)

print("Цветы в букете:")
for flower in bouquet1.flowers:
    print(f"{flower.name} — {flower.price} руб.")

print("Общая стоимость:", bouquet1.get_total_price(), "руб.")
print("Время жизни:", bouquet1.get_lifetime(), "дней")

bouquet1.price_sort()
print("Сортировка по цене:")
for flower in bouquet1.flowers:
    print(f"{flower.name} — {flower.price} руб.")

print("Есть ли роза?", bouquet1.check_flower("Роза"))
print("Есть ли орхидея?", bouquet1.check_flower("Орхидея"))
