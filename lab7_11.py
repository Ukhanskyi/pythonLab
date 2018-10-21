#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Відсортувати слова в рядку по збільшенню їх довжини.


def len_sort(text: str) -> str:
    """Sort words by number of letters"""

    return ' '.join(sorted(text.split(), key=len))

print(len_sort(input("Input your text: ")))
