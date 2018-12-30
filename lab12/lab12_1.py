#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Реалізувати сутність 'точка', яка знає свої координати, вміє визначати відстань до іншої точки. Реалізувати сутність
# 'трикутник', при конструюванні якого передаються три обєкти-точки. Трикутник вміє відповідати на питання чи він
# існує, може обчислити свій периметр і площу.


class Point:
    """ Creates the essence of the vertex """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, point) -> float:
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5


class Triangle:
    """ Creates the essence of the triangle and calculates the lengths of the sides"""

    def __init__(self, a_point, b_point, c_point):
        """Initialization triangle"""

        self.a_point = a_point
        self.b_point = b_point
        self.c_point = c_point
        self.a_side = self.a_point.distance_to(self.b_point)
        self.b_side = self.b_point.distance_to(self.c_point)
        self.c_side = self.c_point.distance_to(self.a_point)

    def is_exist(self) -> bool:
        """Check is exist this triangle"""

        hipotenuse = max(self.a_side, self.b_side, self.c_side)
        cathets_sum = sum(self.a_side, self.b_side, self.c_side) - hipotenuse
        return cathets_sum > hipotenuse

    def get_perimeter(self) -> float:
        """ Calculate his perimeter"""

        if not self.is_exist:
            raise Exception("Triangle not exists")
        return self.a_side + self.b_side + self.c_side

    def get_square(self) -> float:
        """Calculate his square"""

        if not self.is_exist:
            raise Exception("Triangle not exists")
        p = self.get_perimeter() / 2
        return (p * (p - self.a_side) * (p - self.b_side) * (p - self.c_side)) ** 0.5


def input_data() -> Triangle:
    """ Input UI """

    a_point = Point(float(input("Input xa: ")), float(input("Input ya: ")))
    b_point = Point(float(input("Input xb: ")), float(input("Input yb: ")))
    c_point = Point(float(input("Input xc: ")), float(input("Input yc: ")))
    return Triangle(a_point, b_point, c_point)


def output(triangle) -> None:
    """ Output UI """

    try:
        print("Perimeter of triangle:", triangle.get_perimeter())
        print("Perimeter of square:", triangle.get_square())
    except:
        print("Triangle exists:", triangle.is_exist())


output(input_data())
