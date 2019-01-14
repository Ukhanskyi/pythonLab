#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Let h and w be the height and the width dimensions of the rectangular door. Let a, b, c be the dimensions of the box.
# Write a program that determines if there is some way to fit the box through the door.


h = float(input('Enter h door: '))
w = float(input('Enter w door: '))

a = float(input('Enter a box: '))
b = float(input('Enter b box: '))
c = float(input('Enter c box: '))

if a < h and b < w:
    print('The box enters the door')
elif a < h and c < w:
    print('The box enters the door')
elif b < h and c < w:
    print('The box enters the door')
elif a < w and b < h:
    print('The box enters the door')
elif a < w and c < h:
    print('The box enters the door')
elif b < w and c < h:
    print('The box enters the door')
else:
    print('The box will not come in')
