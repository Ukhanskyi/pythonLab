#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Написати програму яка приймає довжини трьох сторін трикутника і видає відповідь чи може такий трикутник існувати.


first_side = int(input('Аirst side of triangle: '))
second_side = int(input('Second side of triangle: '))
third_side = int(input('Third side of triangle: '))

hypotenuse = max(first_side, second_side, third_side)
cathetes_sum = (first_side + second_side + third_side) - hypotenuse

if first_side <= 0 or second_side <= 0 or third_side <= 0:
    print("Triangle does not exist")
elif cathetes_sum > hypotenuse:
    print("Triangle exists")
else:
    print("Triangle does not exist")
