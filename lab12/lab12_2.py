#!/usr/bin/env python3


# Цього разу ми будемо практикуватись в геометричних перетвореннях,
# зокрема обертанням фігур на певний кут. Така функціональність
# характерна для графічних редакторів, але це не єдине застосування
# для них.
# Наприклад, тут Sphere Tag Cloud лежить віджет, що може бути
# використаний для дизайну веб-сторінок. Наведення мишки поверх
# хмари показує її обертання як кулі. Ефект досягнуто реалізацією
# всього двох обертань навколо двох осей (для кожного з плаваючих
# елементів).
# Почнімо з чогось попроще. Уявімо, що ми маємо планарну карту з
# точками на ній. Наприклад, це може бути картина зоряного неба.
# Завдання полягає в обертанні зірок на заданий кут.
# Вхідні дані: файл, що містить першим рядочком кількіть зірочок N і
# кут повороту A (проти годинникової стрілки, від 0 до 360 градусів).
# Наступні рядочки у вхідному файлі містять дані про кожну зірку в формі
# Name X Y. Координати цілі числа, що не перевищують 1000 за абсолютним
# значенням.
# Вихідні дані: текстовий файл з іменами зірок (через пробєл)
# відсортовані у зростаючому порядку за Y координатою (при однаковій
# координаті Y подальше сортування за X)  (координати після
# обертання та заокруглення до найближчого цілого).
# Тест-кейс:
# input file:
# 4 45
# Deneb -10 10
# Algol 10 10
# Sirius -10 -10
# Mira 10 -10
# Output file:
# Sirius Deneb Mira Algol


import math


class Star:
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y

    def rotate(self, angle: int) -> None:
        rad = angle * (math.pi / 180)
        self.x = self.x * math.cos(rad) - self.y * math.sin(rad)
        self.y = self.x * math.sin(rad) + self.y * math.cos(rad)


def input_data() -> list:
    """ UI input your data from file """

    file = open("input.txt", 'rt')
    yield file.readline()
    for line in file:
        data = line.split()
        yield Star(data[0], float(data[1]), float(data[2]))
    file.close()


def rotate_all(stars: list) -> list:
    """ Make rotate figure """

    angle = int(stars.__next__().split()[1])
    for star in stars:
        star.rotate(angle)
        yield star


def output(stars: list) -> None:
    """UI output your data"""

    file = open("output.txt", 'wt')
    stars = list(stars)
    stars.sort(key=lambda star: (star.y, star.x))
    for star in stars:
        file.write(star.name + ' ')
    file.flush()
    file.close()


output(rotate_all(input_data()))
