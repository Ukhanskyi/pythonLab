#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Видалити з рядочка всі зайві пробіли.
# Зайвими вважаються пробіли, що знаходяться  безпосередньо за
# пробілами, тобто. між словами завжди має знаходитись лише один
# пробіл.


def rm_whitespaces(text: str) -> str:
    """Removes unnecessary spaces"""

    return ' '.join(text.split())

print(rm_whitespaces(input("Input your text: ")))
