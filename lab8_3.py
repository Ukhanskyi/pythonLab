#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Дано список з числами, написати функції, що повертають середнє значення і медіану масиву


import functools


def average(source: list) -> float:
    """Search average value """

    return functools.reduce((lambda x, y: x + y), source) / len(source)


def median(source: list) -> float:
    """Search median """

    number = len(source)
    if len(source) % 2 == 1:
        return sorted(source)[number//2]
    else:
        return sum(sorted(source)[number//2-1:number//2+1])/2


print(average([3, 1, 6, 7, 3, 6, 8, 5]))
print(median([3, 1, 6, 7, 3, 6, 8, 5]))
