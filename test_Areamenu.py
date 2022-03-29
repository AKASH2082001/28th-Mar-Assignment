import Areamenu

import pytest

def test_Area_of_Rectangle():
    length = 10
    breadth = 2
    result = Areamenu.Area_of_Rectangle(length,breadth)
    assert result == length*breadth

def test_perimeter_of_rectangle():
    length = 10
    breadth = 20
    result = Areamenu.perimeter_of_rectangle(length,breadth)
    assert result == 2*(length+breadth)

def test_Area_of_Circle():
    radius = 5
    result = Areamenu.Area_of_Circle(radius)
    assert result == 22/7*(radius**2)

def test_Area_of_square():
    sides= 10
    result = Areamenu.Area_of_square(sides)
    assert result == sides**2

def test_Area_of_triangle():
    base =20
    height = 3
    result = Areamenu.Area_of_triangle(base, height)
    assert result == 1/2*(base*height)
