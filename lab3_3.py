#!/usr/bin/env python3
# -*- codding:utf-8 -*-

height = input('Введіть свій зріст у М: ')
weight = input('Введіть свою вагу у  Кг: ')

index = float(weight) / (float(height) ** 2)

print('Індекс маси тіла: ' + str(index))
