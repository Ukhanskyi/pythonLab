#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Написати програму яка приймає ціле додатнє число і результатом роботи якої є відповідь на питання чи є це число
# степенем двійки. Використати бітові операції.


a = int(input('Input int positive number: '))

print(a != 0 and ((a & (a - 1)) == 0))
