#!/usr/bin/env python3
# -*- codding:utf_8 -*-


# Завдання: створити програму що приховує/видобуває текстову інформацію в/з файла-контейнера іншого типу. У якості
# контейнера використати або графічний .bmp 24 bit формат або музичний формат .wav 16 bit stereo 44.1 kHz.  Ідея полягає
# в розміщенні прихованої інформації саме в елементах зображення/звуку, а не в шапках/хвоствиках файла. Розмір
# прихованої тектової інформації до 160 байт (це стандартна довжина для смс повідомлень). Детальніше про стеганографію
# можна ознайомитись тут https://en.wikipedia.org/wiki/Steganography там також є посилання на джерела. Надсилати самі
# контейнери не треба. Програма має працювати з довільними файлами одного з означених форматів. Внесення інформації
# слід реалізувати так щоб, по можливості, це мало впливало на вигляд зображення або звучання музики.


from PIL import Image, ImageDraw
from random import randint


def encrypt_text_in_image():
    """ Codding your information in the image"""

    keys = []  # Тут будуть знаходитись ключі
    img = Image.open(input("path to image: "))  # Створюєм об'єкт зображення
    draw = ImageDraw.Draw(img)  # Об'єкт малювання
    width = img.size[0]  # ширина
    height = img.size[1]  # висота
    pix = img.load()  # всі пікселі тут
    f = open('keys.txt', 'w')  # текстовий файл для ключів

    for elem in ([ord(elem) for elem in input("text here: ")]):
        key = (randint(1, width - 10), randint(1, height - 10))
        g, b = pix[key][1:3]
        draw.point(key, (elem, g, b))
        f.write(str(key) + '\n')
        print('Keys were written to the keys.txt file')
        img.save("new_image.png", "PNG")
    f.close()


encrypt_text_in_image()
