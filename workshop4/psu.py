class PSU:
    def __init__(self, name, model, brand, wattage, efficiency_rating):
        self.__name = name
        self.__model = model
        self.__brand = brand
        self.__wattage = wattage
        self.__efficiency_rating = efficiency_rating
        self.__is_on = False

    def get_on(self):
        return self.__is_on

    def set_on(self, on):
        self.__is_on = on

    def __str__(self):
        return f"---PSU---\n{self.__brand} {self.__name} {self.__model}\nWattage: {self.__wattage}\nEfficiency Rating: {self.__efficiency_rating}\n"

psu = PSU("name", "model", "brand", 240, 4.5)
print(psu)