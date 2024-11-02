from workshop7.rogue import Rogue
from workshop7.warrior import Warrior

class BladeMaster(Warrior, Rogue):
    def __init__(self, strength = 0, crit = 0.0, damage = 40):
        Rogue.__init__(self,critical=crit)
        Warrior.__init__(self, strength)
        Rogue.set_damage(self, damage)
        Warrior.set_damage(self, damage)

    def attack(self):
        return Rogue.attack(self) + Warrior.attack(self)

blademaster = BladeMaster(10,0.25,30)
print(blademaster.attack())

blademaster = BladeMaster(10,crit = 0.65,damage = 37)
print(blademaster.attack())