class Flower:
    def __init__(self, name, color, price, stem_length, freshness, lifetime):
        self.name = name
        self.color = color
        self.price = price
        self.stem_length = stem_length
        self.freshness = freshness
        self.lifetime = lifetime

    def __str__(self):
        return f'{self.name}(цвет: {self.color})'

    def __repr__(self):
        return f'{self.name}(цвет: {self.color})'


class Rose(Flower):
    has_thorns = True

    def __init__(self, color, stem_length, freshness):
        super().__init__("Роза", color, 800, stem_length=stem_length, freshness=freshness, lifetime=4)


class Chrysanthemum(Flower):

    def __init__(self, color, stem_length, freshness):
        super().__init__(
            "Хризантема", color, 400, stem_length=stem_length, freshness=freshness, lifetime=10
        )


class Peony(Flower):

    def __init__(self, color, stem_length, freshness):
        super().__init__("Пион", color, 700, stem_length=stem_length, freshness=freshness, lifetime=8)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def price_of_bouquet(self):
        return sum(flower.price for flower in self.flowers)

    def time_of_withering(self):
        return sum(flower.lifetime for flower in self.flowers) / len(self.flowers)

    def sort_by(self, parameter):
        if parameter == "price":
            return sorted(self.flowers, key=lambda flower: flower.price)
        elif parameter == "stem_length":
            return sorted(self.flowers, key=lambda flower: flower.stem_length)
        elif parameter == "freshness":
            return sorted(self.flowers, key=lambda flower: flower.freshness)
        elif parameter == "color":
            return sorted(self.flowers, key=lambda flower: flower.color)

    def find_by_lifetime(self, min_lifetime):
        return list(filter(lambda flower: flower.lifetime > min_lifetime, self.flowers))

    def __str__(self):
        return ", ".join(str(flower) for flower in self.flowers)

    def __repr__(self):
        return ", ".join(str(flower) for flower in self.flowers)


my_bouquet = Bouquet(
    [Rose('красная', 15, 2), Peony('белый', 10, 3),
     Chrysanthemum('фиолетовая', 20, 1)])
print(my_bouquet.sort_by("stem_length"))
print(my_bouquet.find_by_lifetime(5))
print(my_bouquet.price_of_bouquet())
print(round((my_bouquet.time_of_withering())))
print(my_bouquet)
