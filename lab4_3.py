#!/usr/bin/env python3

import decimal

wage = decimal.Decimal(input('Input your wage: '))
income_tax = decimal.Decimal('0.18')
military_tax = decimal.Decimal('0.015')

all_tax = str(wage * (income_tax + military_tax))

print('You need to pay: ' + all_tax)
