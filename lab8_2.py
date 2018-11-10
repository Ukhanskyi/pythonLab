#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Дано список з числами, написати функції, що повертають середнє значення і медіану масиву


def selection_sort(source: list) -> list:
    """Sort your list """

    for i in range(len(source)):
        min_i = min(source[i:])
        min_index = source[i:].index(min_i)
        source[i + min_index] = source[i]
        source[i] = min_i
    return source


print(selection_sort([3, 1, 5, 7, 3, 6, 8, 0, 5]))
