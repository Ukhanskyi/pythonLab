#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Визначити довжину самого короткого слова в рядку


def smallest_word(text: str) -> str:
    """Find smallest word"""

    return min(text.split())

print(smallest_word(input("Input your text: ")))
