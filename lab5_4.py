#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Написати програму яка приймає коефіцієнти a, b, c квадратного рівняння
# a * x^2 + b * x + c = 0
# і обчислює його корені.
# Тест кейс: a = 1,  b = 5, c = 6 корені -3, -2


a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

if a == 0 and b != 0:
    x1 = x2 = -(c / b)
elif a == 0 and b == 0:
    x1 = x2 = None
else:
    discrim = b ** 2 - 4 * a * c
    x1 = (-b + discrim ** 0.5)/2 * a
    x2 = (-b - discrim ** 0.5)/2 * a
print("x1=" + str(x1) + "\t" + "x2=" + str(x2))
