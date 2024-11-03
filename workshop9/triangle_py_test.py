from triangle import Triangle

def test_area():
    triangle = Triangle(3,4,5)
    assert triangle.calculate_area() == 10
    triangle = Triangle(3, 5, 5)
    assert triangle.calculate_area() == 12.5
    assert triangle.calculate_area() != 12

def test_perimeter():
    triangle = Triangle(3, 4, 5)
    assert triangle.calculate_perimeter() == 12
    triangle = Triangle(3, 5, 5)
    assert triangle.calculate_perimeter() == 13

def test_scale():
    triangle = Triangle(3, 4, 5)
    assert triangle.calculate_area() == 10
    triangle.scale(3)
    assert triangle.calculate_area() == 90
    triangle.scale(5)
    assert triangle.calculate_area() == 2250

def test_semi_perimeter():
    triangle = Triangle(3, 4, 5)
    perimeter = triangle.calculate_perimeter()
    assert triangle.calculate_semi_perimeter() == perimeter / 2
    triangle = Triangle(3, 5, 5)
    perimeter = triangle.calculate_perimeter()
    assert triangle.calculate_semi_perimeter() == perimeter / 2
