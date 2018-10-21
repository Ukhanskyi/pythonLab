#!/usr/bin/env python3
# -*- codding:utf-8 -*-


#    Класичний тест на мінімальну адекватність програміста :)
# Write a program that prints the numbers from 1 to 100. But for
# multiples of three print «Fizz» instead of the number and for the
# multiples of five print «Buzz». For numbers which are multiples of
# both three and five print «FizzBuzz»


def fizzbuzz() -> str:
    """Check is number multiples of three and five"""

    return [(not n % 3) * 'Fizz' + (not n % 5) * 'Buzz' or n for n in range(1, 101)]

print(fizzbuzz())
