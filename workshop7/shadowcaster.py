from workshop7.rogue import Rogue
from workshop7.mage import Mage

class ShadowCaster(Mage, Rogue):
    def __init__(self, magic, crit, damage):
        Mage.__init__(self, magic)
        Rogue.__init__(self, critical=crit)
        Mage.set_damage(self, damage)
        Rogue.set_damage(self, damage)

    def attack(self):
        return Mage.attack(self) + Rogue.attack(self)

shadowcaster = ShadowCaster(10,0.10,10)
print(shadowcaster.attack())

shadowcaster = ShadowCaster(10,crit = 0.80,damage = 10)
print(shadowcaster.attack())