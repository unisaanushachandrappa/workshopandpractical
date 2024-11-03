class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__area = self.calculate_area()

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)

    def scale(self, scale):
        self.__height *= scale
        self.__width *= scale
        self.__area = self.calculate_area()
