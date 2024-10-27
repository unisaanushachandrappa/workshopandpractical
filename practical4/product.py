class Product:
    def __init__(self, id, name, description, price):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__quantity = 0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("price cannot be zero or negative")

    def increase_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity += quantity
        else:
            print("quantity cannot be negative")

    def decrease_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity -= quantity
        else:
            print("quantity cannot be negative")

    def __str__(self):
        return f"Product: {self.get_name()}\nDescription: {self.get_description()}\nQuantity: {self.get_quantity()}\nPrice: ${self.get_price()} each."