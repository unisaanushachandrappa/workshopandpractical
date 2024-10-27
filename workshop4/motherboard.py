from cpu import CPU
from gpu import GPU
from ram import RAM

class Motherboard:
    def __init__(self, name, model, brand, socket, chipset):
        self.__name = name
        self.__model = model
        self.__brand = brand
        self.__socket = socket
        self.__chipset = chipset
        self.__cpu = None
        self.__gpu = None
        self.__ram = []

    def get_name(self):
        return self.__name

    def get_gpu(self):
        return self.__gpu

    def get_cpu(self):
        return self.__cpu

    def install_cpu(self, cpu):
        if isinstance(cpu, CPU):
            self.__cpu = cpu
            print("CPU installed.")
        else:
            print("This part is not compatible.")

    def install_gpu(self, gpu):
        if isinstance(gpu, GPU):
            self.__gpu = gpu
            print("GPU installed.")
        else:
            print("This part is not compatible.")

    def install_ram(self, ram):
        if isinstance(ram, RAM):
            self.__ram.append(ram)
            if len(self.__ram) == 1:
                print("1 RAM installed.")
            if len(self.__ram) > 1:
                print(f"{len(self.__ram)} RAM's installed.")
        else:
            print("This part is not compatible.")

    def __str__(self):
        return f"---MOBO---\n{self.__brand} {self.__model} {self.__name}\nSocket: {self.__socket}\nChipset: {self.__chipset}\n"

mb = Motherboard("name", "model", "brand", 2, "chipset")
print(mb)
print(mb.get_name())
print(mb.get_gpu())
print(mb.get_cpu())
mb.install_cpu(CPU("A", "B", "C", "D", 24))
print(mb.get_cpu())
mb.install_gpu(GPU("A", "B", "C", 128, 240))
print(mb.get_gpu())
mb.install_cpu(GPU("A", "B", "C", 128, 240))
print(mb.get_gpu())
mb.install_gpu(CPU("A", "B", "C", "D", 24))
print(mb.get_cpu())