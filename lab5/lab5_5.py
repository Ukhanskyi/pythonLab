#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Написати програму яка приймає додатне ціле число і видає відповідь чи це число є простим.
# https://uk.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE
# Використати цикл while.


numb = int(input('Input numb: '))

if numb > 1:
    i = 2
    while i != int(numb ** 0.5) + 1:
        if (numb % i) == 0:
            print('This is not a simple number')
            break
        i += 1
    else:
        print('This is a simple number')
else:
    print('This is not a simple number')
