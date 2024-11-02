from mage import Mage
from warrior import Warrior

class BattleMage(Mage, Warrior):
    def __init__(self, *args, magic = 0, strength = 0):
        if len(args) > 0:
            Mage.__init__(self, args[1])
            Warrior.__init__(self, args[0])
            Mage.set_damage(self, args[2])
            Warrior.set_damage(self, args[2])
        else:
            Mage.__init__(self, magic)
            Warrior.__init__(self, strength)
            Mage.set_damage(self,30)
            Warrior.set_damage(self,30)

    def attack(self):
        return Mage.attack(self) + Warrior.attack(self)

battlemage = BattleMage(10,10,10)
print(battlemage.attack())

battlemage = BattleMage(strength = 10,magic = 10)
print(battlemage.attack())

battlemage = BattleMage(10,100,1000)
print(battlemage.attack())