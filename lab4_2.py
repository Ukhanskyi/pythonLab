#!/usr/bin/env python3
# *-* codding:utf-8 *-*


# Вхідні дані: Три дійсних числа вводяться користувачем програми
# Вихідні дані: результат обчислення формули: 1/(d*math.sqrt(2*pi))*exp(-((a-b)**2)/(2*d**2))
# Для перевірки:
# Вхідні дані: 1 1 0.25
# Результат: 1.59576912161


import math

exp = math.exp
pi = math.pi

numb1 = input("Введіть перше число: ")
numb2 = input("Введіть друге число: ")
numb3 = input("Введіть третє число: ")

a = float(numb1)
b = float(numb2)
d = float(numb3)

function = 1/(d*math.sqrt(2*pi))*exp(-((a-b)**2)/(2*d**2))

print(function)
