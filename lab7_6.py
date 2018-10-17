#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Написати функцію, що приймає рядок і друкує його в рамці з зірочок.
# Тест-кейс:
# input string: 'Hello, world!'
# output
# *****************
# * Hello, world! *
# *****************


def ui_input() -> str:
    """Input your text"""

    text = input('Input your text: ')

    return(text)


def cute_output(text: str) -> str:
    """Create border * """

    print('*' * len(text) + "****")
    print("*", text, "*")
    print('*' * len(text) + "****")

cute_output(ui_input())
