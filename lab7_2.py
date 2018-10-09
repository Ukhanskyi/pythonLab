#!/usr/bin/env python3
# -*- codding:utf-8 -*-

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
