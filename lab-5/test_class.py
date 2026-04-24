import pytest
from triangle_class import Triangle, IncorrectTriangleSides

# Позитивные тесты
def test_equilateral_triangle():
    t = Triangle(5, 5, 5)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 15

def test_isosceles_triangle():
    t = Triangle(5, 5, 3)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 13

def test_nonequilateral_triangle():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12

# Негативные тесты
def test_invalid_sides_negative():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 2, 3)

def test_invalid_sides_zero():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 4, 5)

def test_invalid_triangle_inequality():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 10)

def test_invalid_type_string():
    with pytest.raises(IncorrectTriangleSides):
        Triangle("a", 2, 3)