import math
from typing import List


class Shape:
    def perimeter(self) -> float:
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = a, b, c

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def area(self) -> float:
        p = self.perimeter() / 2
        expr = p * (p - self.a) * (p - self.b) * (p - self.c)
        if expr < 0:
            return 0
        return expr**0.5


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width, self.height = width, height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def area(self) -> float:
        return self.width * self.height


class Trapeze(Shape):
    def __init__(self, a: float, b: float, c: float, d: float):
        self.a, self.b, self.c, self.d = a, b, c, d

    def perimeter(self) -> float:
        return self.a + self.b + self.c + self.d

    def area(self) -> float:
        s = (self.a + self.b + self.c + self.d) / 2
        expr = s * (s - self.a) * (s - self.b) * (s - self.c) * (s - self.d)
        if expr < 0 or self.a == self.b:
            return 0
        h = (2 / abs(self.a - self.b)) * math.sqrt(expr)
        return 0.5 * (self.a + self.b) * h


class Parallelogram(Shape):
    def __init__(self, a: float, b: float, h: float):
        self.a, self.b, self.h = a, b, h

    def perimeter(self) -> float:
        return 2 * (self.a + self.b)

    def area(self) -> float:
        return self.a * self.h


class Circle(Shape):
    def __init__(self, r: float):
        self.r = r

    def perimeter(self) -> float:
        return float(2 * math.pi * self.r)

    def area(self) -> float:
        return float(math.pi * self.r ** 2)


def parse_shape(line: str) -> Shape:
    parts = line.split()
    shape_type = parts[0]
    values = list(map(float, parts[1:]))

    if shape_type == "Triangle":
        return Triangle(*values)
    elif shape_type == "Rectangle":
        return Rectangle(*values)
    elif shape_type == "Trapeze":
        return Trapeze(*values)
    elif shape_type == "Parallelogram":
        return Parallelogram(*values)
    elif shape_type == "Circle":
        return Circle(*values)


def find_max_shapes(filename: str):
    with open(filename, 'r') as file:
        shapes = [parse_shape(line) for line in file]

    max_area_shape = max(shapes, key=lambda s: s.area())
    max_perimeter_shape = max(shapes, key=lambda s: s.perimeter())

    return max_area_shape, max_perimeter_shape

print('file 1')
file_name = "input01.txt"
max_area, max_perimeter = find_max_shapes(file_name)
print(f"Фігура з найбільшою площею: {type(max_area).__name__}, площа = {max_area.area()}")
print(f"Фігура з найбільшим периметром: {type(max_perimeter).__name__}, периметр = {max_perimeter.perimeter()}")
print('file 2')
file_name = "input02.txt"
max_area, max_perimeter = find_max_shapes(file_name)
print(f"Фігура з найбільшою площею: {type(max_area).__name__}, площа = {max_area.area()}")
print(f"Фігура з найбільшим периметром: {type(max_perimeter).__name__}, периметр = {max_perimeter.perimeter()}")
print('file 3')
file_name = "input03.txt"
max_area, max_perimeter = find_max_shapes(file_name)
print(f"Фігура з найбільшою площею: {type(max_area).__name__}, площа = {max_area.area()}")
print(f"Фігура з найбільшим периметром: {type(max_perimeter).__name__}, периметр = {max_perimeter.perimeter()}")
