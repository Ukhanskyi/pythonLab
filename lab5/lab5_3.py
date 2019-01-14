#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Написати програму, що грає в гру "Камінь, ножиці, папір" з людиною. Правила гри тут
# (Для генерації випадкового рішення компютером можна скористатись функціями з модуля random)


import random

user = int(input("Choose : \t 1.Rock \t 2.Scissors \t 3.Paper \n"))

comp = random.randint(1, 3)

if user == 1 and comp == 2:
    print('It is Scissors! \n You Win!!!')
elif user == 2 and comp == 3:
    print('It is Paper! \n You Win!!!')
elif user == 3 and comp == 1:
    print('It is Rock! \n You Win!!!')
elif user == 2 and comp == 1:
    print('It is Rock! \n You Louser!!!')
elif user == 3 and comp == 2:
    print('It is Scissors! \n You Louser!!!')
elif user == 1 and comp == 3:
    print('It is Paper! \n You Louser!!!')
else:
    print("Draw")
    if comp == 1:
        print("It\'s Rock")
    elif comp == 2:
        print("It\'s Scissors")
    elif comp == 3:
        print("It\'s Paper")
    else: pass


