#!/usr/bin/env python3
# -*-codding:utf-8 -*-


#   Гра Blackjack має дуже прості правила: гравці беруть карти по одній
# намагаючись зібрати більше ніж опонент, але не перевищуючи 21. Набір
# карт містить карти від 2 до 10 включно, які рахуються за іх номіналом,
# також Король, Дама, Валет, що коштують по 10 кожна а також Туз, який
# може бути 1 або 11 в залежності від того що краще. Вхід програми
# декілька карт представлені символами: 2, 3, 4, 5, 6, 7, 8, 9;  T, J,
# Q, K для 10, Валет, Дама, Король; А - для Туза. Результат роботи
# кількість очок що не перевищує 21, або слово 'Bust' якщо сума більша
# за 21 (цей гравець відразу програє).


def calculate_cards(cards: str) -> int:
    """Calculate your card in BlackJack """

    cards = cards.split()
    card_table = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, "K": 10,\
                  'A': 0}
    total = sum([card_table[_] for _ in cards])
    if 'A' in cards:
        ace_score = 21 - total
        if ace_score < 11:
            total = total + 1
        elif ace_score > 11:
            total = total + 11
        else:
            total = total + ace_score
    return total


def output(result: int) -> None:
    """Out your cards or bust"""

    if result > 21:
        print("Bust")
    elif result == 21:
        print("You have BlackJack!!!")
    else:
        print(result)


output(calculate_cards(input("Input your cards: ")))
