#!/usr/bin/env python3

numb = int(input('Input numb: '))

if numb > 1:
    i = 2
    while i != int(numb ** 0.5) + 1:
        if (numb % i) == 0:
            print('This is not a simple number')
            break
        i += 1
    else:
        print('This is a simple number')
else:
    print('This is not a simple number')
