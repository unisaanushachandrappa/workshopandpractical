class CPU:
    def __init__(self, name, model, brand, socket, cores):
        self.__name = name
        self.__model = model
        self.__brand = brand
        self.__socket = socket
        self.__cores = cores

    def __str__(self):
        return f"---CPU---\n{self.__brand} {self.__model} {self.__name} Processor\nSocket: {self.__socket}\nCores: {self.__cores}\n"


cpu = CPU("A", "B", "C", "D", 24)
print(cpu)