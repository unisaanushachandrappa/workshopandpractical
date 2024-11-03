class Triangle:
    def __init__(self, hypotenuse, opposite, adjacent):
        self.hypotenuse = hypotenuse
        self.opposite = opposite
        self.adjacent = adjacent

    def calculate_area(self):
        return 0.5 * self.opposite * self.adjacent

    def calculate_perimeter(self):
        return self.hypotenuse + self.opposite + self.adjacent

    def scale(self, factor):
        self.hypotenuse *= factor
        self.opposite *= factor
        self.adjacent *= factor

    def calculate_semi_perimeter(self):
        return self.calculate_perimeter() / 2