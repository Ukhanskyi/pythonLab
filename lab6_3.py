#!/usr/bin/env python3

import decimal
import math

def ui_input() -> list:
    """Input"""

    money = decimal.Decimal(input("Input amount of money: "))
    procent = decimal.Decimal(input("Input interest rate of the bank: "))
    final_money = decimal.Decimal(input("Input final amount of money: "))

    return [money, procent, final_money]

def ui_output(result: str) -> None:
    """Output"""

    result = str(result)
    print("Duration of deposit: ", result)

def deposit_duration_calculate(deposit: list) -> float:
    """Calcucate"""

    duration = math.log(deposit[2] / deposit[0], (1 + deposit[1] / 100))

    return duration

ui_output(deposit_duration_calculate(ui_input()))
