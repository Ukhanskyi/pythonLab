#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Слово або ціла фраза, букви якої ідуть в тому ж порядку якщо їх читати
# зліва-направо, або справа-наліво, називається паліндромом. Ось дескілька
# прикладів:

# 1) Was it a cat I saw
# 2) No 'x' in Nixon
# 3) А роза упала на лапу Азора
# 4) Три психи пили Пилипихи спирт
# 5) Вор Азаров

# регістр букв не враховується. Пробєли і знаки також.
# Задача цієї вправи, написати функцію, що визначає чи є фраза паліндромом чи
# ні (повертає bool True/False).


def ui_input() -> str:
    """Enter sentence"""

    a = str(input('Enter sentence: '))

    return(a)

def revers(a: str) -> bool:
    """Turns the sentences back forward"""

    a = a.lower().replace(' ', '')
    a = a.lower().replace('\'', '')

    b = a[::-1]

    c = a == b

    return(c)

def ui_out(c: str) -> bool:
    """Out a == b"""
    print(c)

ui_out(revers(ui_input()))
