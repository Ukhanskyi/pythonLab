#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Написати програму генерації пароля. Пароль має бути не менше 8
# випадкових маленьких та великих символів, містити хоча б одну цифру
# та спецсимвол.


import random
import string

def gen_password() -> str:
    """Generate valid password"""

    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation
    while not set(string.digits).intersection(set(password)) or \
    not set(string.punctuation).intersection(set(password)):
        password = ''.join(random.choice(chars) for i in range(random.randint(8, 16)))
    return password

print(gen_password())
