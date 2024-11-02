from abc import ABC, abstractmethod

class Armour(ABC):
    def __init__(self, material, defence, toughness, durability):
        self.__material = material
        self.__defence = defence
        self.__toughness = toughness
        self.__durability = durability
        self.__protection = self.calculate_protection()

    def get_defence(self):
        return self.__defence

    def get_toughness(self):
        return self.__toughness

    @abstractmethod
    def calculate_protection(self):
        pass

    def reduce_durability(self, amount):
        self.__durability -= amount
        if self.__durability < 0:
            self.__durability = 0
        self.__protection = self.calculate_protection()

    def repair(self, amount):
        self.__durability += amount

    def is_broken(self):
        return self.__durability == 0

    def __str__(self):
        return (f"---{self.__material.upper()} {self.__class__.__name__.upper()}--\n"
                f"Defence: {self.__defence}\n"
                f"Toughness: {self.__toughness}\n"
                f"Durability: {self.__durability}\n"
                f"{self.__class__.__name__} protection = {self.__protection} ")