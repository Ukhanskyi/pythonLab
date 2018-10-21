#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Дано e-mail в рядку. Визначити, чи є він коректним (наявність символа
# '@' і точки, наявність не менше двох символів після останньої точки
# і т. д).


def is_valid_email(email: str) -> bool:
    """Check is valid your password"""

    splited = email.split('@')[1].split('.')
    return len(splited[-1]) > 1 and email.count('@') < 2 and len(splited) > 1

print(is_valid_email(input("Input your email: ")))
