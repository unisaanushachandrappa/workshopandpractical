from circle import Circle

def test_area():
    circle = Circle(5)
    assert circle.calculate_area() == 78.5
    circle = Circle(2)
    assert circle.calculate_area() == 12.56

def test_perimeter():
    circle = Circle(5)
    assert 31.40 == round(circle.calculate_perimeter(), 2)
    circle = Circle(2)
    assert 12.56 == round(circle.calculate_perimeter(), 2)

def test_scale():
    circle = Circle(5)
    assert 78.5 == circle.calculate_area(), 2
    circle.scale(2)
    assert 314 == circle.calculate_area(), 2
    circle.scale(3)
    assert 2826 == circle.calculate_area(), 2
