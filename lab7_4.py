#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Написати функцію, що здійснює елементарне шифрування повідомлення
# - рядка шляхом заміни кожної літери сусідньою справа за абеткою.
# 'а' міняється на 'b', 'q' на 'r', і так далі. Слово 'vasia' буде
# зашифроване як 'wbtjb'


def ui_input() ->str:

    """Enter your text"""
    text = input('Input your text: ')

    return(text)

def codding_text(text: str) -> str:
    """Codding the text shifting to 1 letter right"""

    cod_text = list(map(lambda x: chr(ord(x) + 1), text))

    return ''.join(cod_text)

def ui_output(cod_text: str) -> str:
    """Out codding text"""

    print(cod_text)

ui_output(codding_text(ui_input()))
