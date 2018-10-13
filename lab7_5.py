#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Це нескладне завдання для ознайомлення з обробкою рядків. Треба
# написати програму яка для рядку англ. текста повертає кількість
# голосних літер в ньому (тобто. літер a, o, u, i, e, y). Зверніть
# увагу, що 'у'  в цьому завданні голосна. Недивлячись на простоту,
# ця технологія важлива і використовується в криптографії.


def ui_input() -> str:
    """Enter your text"""

    text = input('Input your text (In English): ')

    return(text)

def find_vowel(text: str) -> str:
    """Find in all text vowel letter"""

    vowel = text.count('a') + text.count('o') + text.count('u') +\
    text.count('i') + text.count('e') + text.count("y")

    return(vowel)

def ui_output(vowel: str) -> str:
    """Output vowel letter"""

    print(vowel)

ui_output(find_vowel(ui_input()))
