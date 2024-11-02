from armour import Armour
class Helmet(Armour):
    def calculate_protection(self):
        if self.is_broken():
            return 0.0
        else:
            return self.get_defence() + (self.get_toughness() * 0.5)

helmet = Helmet("Steel", 100, 100, 50)
helmet.reduce_durability(100)
print(helmet)

helmet = Helmet("Steel", 100, 100, 50)
print(helmet)