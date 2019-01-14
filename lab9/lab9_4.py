#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Написати функції для перетворення чисел і римську форму запису і навпаки. Числа в діапазоні від 0 до 3999 включно


def num_list(number: int) -> list:
    """ Checking your number """

    number_str = str(number)
    count = 1
    for digit in number_str[::-1]:
        if digit != '0':
            yield int(digit) * count
        count *= 10


def to_roman(arabic: int) -> str:
    """ Translate to Roman number """

    roman_numeral = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI',
                     7: 'VII', 8: 'VII', 9: 'IX', 10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL',
                     50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC',
                     300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC',
                     900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM'}
    return ''.join([roman_numeral.get(num) for num in num_list(arabic)][::-1])


def to_arabic(roman: str):
    """ Translate to Arabic number """

    roman = roman.upper()
    keys = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
    arabic = {'IV': '4', 'IX': '9', 'XL': '40', 'XC': '90', 'CD': '400', 'CM': '900',
                    'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}
    for key in keys:
        if key in roman:
            roman = roman.replace(key, ' {}'.format(arabic.get(key)))
    return sum(int(num) for num in roman.split())


print(to_roman(input("Input arabic digits: ")))
print(to_arabic(input("Input roman digits: ")))
