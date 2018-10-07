#!/usr/bin/env python3

import decimal

def ui_input() -> list:
    """Input"""

    money = decimal.Decimal(input("Input amount of money: "))
    procent = decimal.Decimal(input("Input interest rate of the bank: "))
    duration = decimal.Decimal(input("Input duration in years: "))

    return [money, procent, duration]

def ui_output(result: str) -> None:
    """Output"""

    result = str(result)
    print("Final amount of money: ", result)

def deposit_calculate(deposit: list) -> float:
    """Calcucate"""

    if len(deposit) != 3:
        print("Too many or less members of list")
        exit()

    final_money = deposit[0] * (1 + deposit[1] / 100) ** deposit[2]

    return final_money

ui_output(deposit_calculate(ui_input()))
