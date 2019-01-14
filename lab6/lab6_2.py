#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Ви хочете придбати автомобіль який коштує $10000. Однак, зараз у вас є $1000. Один зі шляхів збільшити суму грошей це
# покласти їх на депозит до банку. Наприклад, якщо рахунок зростатиме на 8% щороку ви зможете отримати потрібну суму
# усього за 30 років. Більше того, якщо за умовами депозиту оновлення рахунку здійснюється не щороку а щомісяця (при тій
# самій річній процентній ставці) ви зможете зібрати потрібну суму всьго за 29 років! Прикольно :)  В цьому завданні вам
# необхідно написати функцію, яка приймає наявну суму, річну процентну ставку банку і тривалість депозиту в роках і
# повертає суму на момент завершення депозитної угоди.


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
    """Calculate"""

    if len(deposit) != 3:
        print("Too many or less members of list")
        exit()

    final_money = deposit[0] * (1 + deposit[1] / 100) ** deposit[2]

    return final_money


ui_output(deposit_calculate(ui_input()))
