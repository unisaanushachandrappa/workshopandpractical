class Mage:
    def __init__(self, *args):
        if len(args) == 1:
            self.__magic = args[0]
            self.__damage = 15
        elif len(args) > 1:
            self.__magic = args[0]
            self.__damage = args[1]

    def attack(self):
        return self.__damage * (self.__magic / 10)

    def set_damage(self, damage):
        self.__damage = damage

# mage = Mage(100)
# print(mage.attack())
#
# mage = Mage(100,10)
# print(mage.attack())