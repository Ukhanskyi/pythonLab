#!/usr/bin/env python3
# -*- codding:utf-8 -*-

import math

numb1 = input("Введіть перше невід'ємне число: ")
numb2 = input("Введіть друге невід'ємне число: ")
e = math.e

a = float(numb1)
b = float(numb2)

x=(math.sqrt(a*b))/((e**a)*b)+(a*e**((2*a)/b))

print(x)
