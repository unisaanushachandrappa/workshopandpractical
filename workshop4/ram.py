class RAM:
    def __init__(self, name, model, brand, ddr, size, speed):
        self.__name = name
        self.__model = model
        self.__brand = brand
        self.__ddr = ddr
        self.__size = size
        self.__speed = speed

    def __str__(self):
        return f"---RAM---\n{self.__brand} {self.__name} {self.__model} DDR{self.__ddr}\nSize: {self.__size}GB\nSpeed: {self.__speed}MHz\n"

ram = RAM("name", "model", "brand", "ddr", 10, 200)
print(ram)