#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Дано два рядки. Завдання визначити, чи можна з деяких символів
# першого рядка утворити другий рядок.


def isAnagram(text1, text2: str) -> bool:
    """Check is anagram two string"""

    return not[0 for _ in text1 if text1.count(_) > text2.count(_)]

print(isAnagram(input('Input your text 1: '), input('Input your text 2: ')))

