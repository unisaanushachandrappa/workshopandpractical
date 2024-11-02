from armour import Armour

class Boot(Armour):
    def calculate_protection(self):
        if self.is_broken():
            return 0.0
        else:
            return self.get_defence() + (self.get_toughness() * 0.6)