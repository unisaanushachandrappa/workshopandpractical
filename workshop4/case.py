from motherboard import Motherboard
from psu import PSU

class Case:
    def __init__(self, name, model, brand):
        self.__name = name
        self.__model = model
        self.__brand = brand
        self.__motherboard = None
        self.__psu = None

    def get_motherboard(self):
        return self.__motherboard

    def get_psu(self):
        return self.__psu

    def install___motherboard(self, motherboard):
        if isinstance(motherboard, Motherboard):
            self.__motherboard = motherboard
        else:
            print("not a valid motherboard")

    def install_psu(self, psu):
        if isinstance(psu, PSU):
            self.__psu = psu
        else:
            print("not a valid PSU")

    def __str__(self):
        return f"---CASE---\n{self.__brand} {self.__name} {self.__model} Case\n"

case = Case("Barry", "test", "Toxic")
print(case)