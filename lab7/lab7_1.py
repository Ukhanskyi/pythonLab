#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Обертання строки на k символів означає операцію зсуву елементів рядка
# на k позицій. Символи, що виходять за межі рядка заходять з іншого боку
# по колу. Якщо k відємне, зсув здійснюється в інший бік. Написати функцію,
# яка приймає рядок і ціле число на яке здійснюється обертання. k не перевищує
# половини довжини рядка.

# Тест-кейси:

# 'forwhomthebelltolls', 3       результат         whomthebelltollsfor
# 'verycomplexnumber',  -6       результат         numberverycomplex


def ui_input() -> list:
    """Input your data """

    your_string = input('Input your string: ')
    need_numb_shift = int(input('Enter number'))

    return [your_string, need_numb_shift]

def shift_str(string: list) -> str:
    """Shift your string """

    first_str = string[0][0: string[1]]
    second_str = string[0][string[1] :]

    new_string = second_str + first_str

    return(new_string)

def ui_out(new_string: str) -> str:
    """Out data"""

    print(new_string)

ui_out(shift_str(ui_input()))
