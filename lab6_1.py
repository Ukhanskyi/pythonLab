#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Можливість обчислити площу трикутника дуже важлива адже багато складних практичних задач зводяться до неї. В цьому
# завданні вам треба написати функцію мовою Пайтон, яка приймає довжини трьох сторін трикутника і повертає його площу.


def ui_input_side_triangle() -> list:
    """Enter 3 side triangle"""

    a = float(input('Enter first side: '))
    b = float(input('Enter second side: '))
    c = float(input('Enter third side: '))
    return [a, b, c]


def calc_area_triangle(sides: list) -> float:
    """Calculating area triangle"""

    # calculate the semi-perimeter
    s = (sides[0] + sides[1] + sides[2]) / 2

    # calculate the area
    area = (s * (s - sides[0]) * (s - sides[1]) * (s - sides[2])) ** 0.5
    return area


def ui_output_area_triangle(area: float) -> float:
    """Output area triangle on console"""

    # out area triangle
    print('The area of the triangle is %0.2f' % area)


out = calc_area_triangle(ui_input_side_triangle())
print(out)
