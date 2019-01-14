#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# У прикладеному файлі знаходиться реальний лог веб сервера nginx за добу. Завдання обчислити сумарну кількість
# надісланих та прийнятих байтів. Оскільки такий протокол може бути дуже великим слід застосувати способи що не
# потребують завантаження в память усього вмісту, наприклад генераторні вирази.


def parse(filename: str) -> int:
    """Open file nginx and find size """

    f = open(filename, 'rt')
    for line in f:
        size = line.split()[9]
        yield int(size)


def output(bytes: list) -> int:
    """ Calculate byte and output size nginx"""

    byte_size = 0
    for byte in bytes:
        byte_size += byte
    print("Size nginx equals:\t\t", byte_size, "bytes!")


output(parse("2017_05_07_nginx.txt"))
