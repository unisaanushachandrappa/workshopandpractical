class Warrior:
    def __init__(self, *args):
        if len(args) == 1:
            self.__strength = args[0]
            self.__damage = 20
        elif len(args) > 1:
            self.__strength = args[0]
            self.__damage = args[1]

    def attack(self):
        return self.__damage + self.__strength

    def set_damage(self, damage):
        self.__damage = damage

# warrior = Warrior(10,200)
# print(warrior.attack())
#
# warrior = Warrior(10)
# print(warrior.attack())