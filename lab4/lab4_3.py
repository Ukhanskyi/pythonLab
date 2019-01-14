#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Написати прогаму яка для отриманого працівником місячного доходу обчислює суми податків, що необхідно сплатити до
# бюджету. Усі обчислення слід виконати з типом даних decimal. Податок на доходи фізичних осіб 18%, військовий збір 1.5%


import decimal

wage = decimal.Decimal(input('Input your wage: '))
income_tax = decimal.Decimal('0.18')
military_tax = decimal.Decimal('0.015')

all_tax = str(wage * (income_tax + military_tax))

print('You need to pay: ' + all_tax)
