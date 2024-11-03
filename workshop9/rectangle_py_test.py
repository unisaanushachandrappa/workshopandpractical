from rectangle import Rectangle

def test_area():
    rectangle = Rectangle(3, 4)
    assert rectangle.calculate_area() == 12
    rectangle = Rectangle(8, 6)
    assert rectangle.calculate_area() == 48

def test_perimeter():
    rectangle = Rectangle(3,4)
    assert 14 == rectangle.calculate_perimeter()
    rectangle = Rectangle(8, 6)
    assert 28 == rectangle.calculate_perimeter()

def test_scale():
    rectangle = Rectangle(3, 4)
    assert rectangle.calculate_area() == 12
    rectangle.scale(2)
    assert rectangle.calculate_area() == 48
    rectangle.scale(3)
    assert rectangle.calculate_area() == 432