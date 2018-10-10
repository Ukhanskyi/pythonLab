#!/usr/bin/env python3
# -*- cidding:utf-8 -*-


# Нам дано рядки, що містять дужки 4 видів - круглі (), квадратні [],
# фігурні {} і кутові <>. Задача в тому, щоб перевірити чи є послідовність
# дужок коректною. Тобто, будь-яка відкриваюча дужка повинна мати закриваючу
# того ж типу десь далі по рядку, і крім того, пари дужок не повинні
# перетинатись, однак вони можуть бути вкладеними:

# (a+[b*c] - {d/3})         - ок
# (a+[b*c) - 17]            - не ок, перетинаються

# Написати булеву функцію, що повертає True якщо дужки розставлено вірно або
# False інакше.
# Тест кейси
# (((a * x) + [b] * y) + c  		 False
# auf(zlo)men [gy<psy>] four{s}          True


def ui_input() -> str:
    """Enter your expression"""

    expression = input("Input your string: ")

    return(expression)

def rejecting_brackets(expression: str) -> str:
    """ Сhecks the correct positioning of the brackets """

    open_brackets = tuple('([{<')
    close_brackets = tuple(')]}>')
    mapping = dict(zip(open_brackets, close_brackets))
    queue = []

    for letter in expression:
        if letter in open_brackets:
            queue.append(mapping[letter])
        elif letter in close_brackets:
            if not queue or letter!= queue.pop():
                print(False)

def ui_output(queue: list) -> list:
    """ Output """

    print(not queue)

ui_output(rejecting_brackets(ui_input()))
