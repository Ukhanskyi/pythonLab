#!/usr/bin/env python3
# -*-codding:utf-8 -*-


# Написати програму що перетворює числове представлення грошової суми в суму прописом. Наприклад Вхід: 1234.56.
# Вихід: Одна тисяча двісті тридцять чотири гривні 56 копійок. Вхідне число не перевищує 999999.99. Така функція
# застосовується при формуванні платіжних доручень, накладних, рахунків і т. д.


def convert_to_text(your_number: float) -> str:
    """ Convert your number into text """

    if your_number > 999999.99:
        raise ValueError('Not supporter over million')
    sample = []
    numbers = {1: 'один', 2: 'два', 3: 'три', 4: 'чотири', 5: 'п\'ять', 6: 'шість',
               7: 'сім', 8: 'вісім', 9: 'дев\'ять', 10: 'десять', 11: 'одинадцять',
               12: 'дванадцять', 13: 'тринадцять', 14: 'чотирнадцять', 15: 'п\'ятнадцять',
               16: 'шістнадцять', 17: 'сімнадцять', 18: 'вісімнадцять', 19: 'дев\'ятнадцять',
               20: 'двадцять', 30: 'тридцять', 40: 'сорок', 50: 'п\'ятдесят', 60: 'шістдесят',
               70: 'сімдесять', 80: 'вісімдесять', 90: 'дев\'яносто', 100: 'сто',
               200: 'двісті', 300: 'триста', 400: 'чотириста', 500: 'п\'ятсот', 600: 'шістсот',
               700: 'сімсот', 800: 'вісімсот', 900: 'дев\'ятсот', 0: ''}
    first = list(str(int(your_number * 100)))
    rate = 5
    index = -(rate + 2)
    while first[index] == '1' and index != -1:
        first[index] += first[index + 1]
        first[index + 1] = '0'
        index += 3
    while len(first) > rate:
        popped = first.pop(0)
        sample.append(numbers[int(popped) * 10 ** (len(first) - len(popped) - rate + 1)])
    if "один" in sample:
        sample[sample.index("один")] = "одна"
        sample.append("тисяча")
    elif "два" in sample:
        sample[sample.index("два")] = "дві"
        sample.append("тисячі")
    elif "три" in sample:
        sample[sample.index("три")] = "три"
        sample.append("тисячі")
    elif "чотири" in sample:
        sample[sample.index("чотири")] = "чотири"
        sample.append("тисячі")
    else:
        sample.append("тисяч")
    rate -= 3
    while len(first) > rate:
        popped = first.pop(0)
        sample.append(numbers[int(popped) * 10 ** (len(first) - len(popped) - rate + 1)])
    if "один" in sample:
        sample[sample.index("один")] = "одна"
        sample.append("гривня")
    elif "два" in sample:
        sample[sample.index("два")] = "дві"
        sample.append("гривні")
    elif "три" in sample:
        sample[sample.index("три")] = "три"
        sample.append("гривні")
    elif "чотири" in sample:
        sample[sample.index("чотири")] = "чотири"
        sample.append("гривні")
    else:
        sample.append("гривень")
    coins = int(''.join(first))
    sample.append(str(coins))
    if 10 < coins < 20:
        sample.append("копійок")
    elif 1 < coins % 10 < 5:
        sample.append("копійки")
    elif coins % 10 == 1:
        sample.append("копійка")
    else:
        sample.append("копійок")
    return ' '.join(' '.join(sample).split()).capitalize()


print(convert_to_text(float(input("Input your amount: "))))
