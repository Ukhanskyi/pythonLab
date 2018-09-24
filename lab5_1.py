#!/usr/bin/env python3

a = int(input('Input int positive number: '))

print(a != 0 and ((a & (a - 1)) == 0))
