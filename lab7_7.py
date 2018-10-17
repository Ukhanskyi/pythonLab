#!/usr/bin/env python3
# -*- codding:utf-8 -*-

# Написати дві функції, які в заданому рядку знаходять імена змінних
# і замінюють написання з camel_case на snakeCase і навпаки.
# Тест кейс:
# вхід: 'print([res_square ** 2 for res_square in input_array if
# res_square > 18 ])'
# вихід: 'print([resSquare ** 2 for resSquare in inputArray if
# resSquare > 18 ])'

import re

def camel_case(text: str) -> str:
    """Make text from SnakeCase to camel_case"""

    words = text.split('_')
    camel_name = words[0]
    camel_name += ''.join(list(map(str.capitalize, words[1:])))

    return camel_name

def snake_case(text: str) -> str:
    """Make text from camel_case to SnakeCase"""

    words = re.sub(r'([A-Z])', r" \1", text).split()
    snake_name = '_'.join(list(map(str.lower, words)))

    return snake_name

print(camel_case(input("Input your text in camel_case. What will be transformed in snakeСase: ")))
print(snake_case(input("Input your text in SnakeCase. What will be transformed in camel_case: ")))
