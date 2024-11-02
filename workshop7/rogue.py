class Rogue:
    def __init__(self, *args, critical = 0):
        if len(args) == 1:
            self.__damage = args[0]
            self.__critical = 1
            self.__critical_chance = 0.25
        elif len(args) > 1:
            self.__damage = args[0]
            self.__critical = args[1]
            self.__critical_chance = 0.25
        else:
            self.__damage = 10
            self.__critical = critical
            self.__critical_chance = 0.25

    def attack(self):
        if self.__critical > self.__critical_chance:
            return self.__damage * self.__damage
        else:
            return self.__damage

    def set_damage(self, damage):
        self.__damage = damage

# rogue = Rogue()
# print(rogue.attack())
#
# rogue = Rogue(10,0.65)
# print(rogue.attack())
#
# rogue = Rogue(critical=0.65)
# print(rogue.attack())
#
# rogue = Rogue(25)
# print(rogue.attack())