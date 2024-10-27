class GPU:
    def __init__(self, name, model, brand, memory, clock_speed):
        self.__name = name
        self.__model = model
        self.__brand =  brand
        self.__memory = memory
        self.__clock_speed = clock_speed

    def __str__(self):
        return f"---GPU---\n{self.__brand} {self.__model} {self.__name}\nMemory: {self.__memory}GB\nClock Speed: {self.__clock_speed}MHz\n"

gpu = GPU("A", "B", "C", 128, 240)
print(gpu)