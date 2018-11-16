#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Завдання: створити програму що приховує/видобуває текстову інформацію в/з файла-контейнера іншого типу. У якості
# контейнера використати або графічний .bmp 24 bit формат або музичний формат .wav 16 bit stereo 44.1 kHz.  Ідея полягає
# в розміщенні прихованої інформації саме в елементах зображення/звуку, а не в шапках/хвоствиках файла. Розмір
# прихованої тектової інформації до 160 байт (це стандартна довжина для смс повідомлень). Детальніше про стеганографію
# можна ознайомитись тут https://en.wikipedia.org/wiki/Steganography там також є посилання на джерела. Надсилати самі
# контейнери не треба. Програма має працювати з довільними файлами одного з означених форматів. Внесення інформації
# слід реалізувати так щоб, по можливості, це мало впливало на вигляд зображення або звучання музики.


from PIL import Image
from re import findall


def decrypt_your_message():
    """ Decrypt your text from the image"""

    a = []
    keys = []
    img = Image.open(input("path to image: "))

    pix = img.load()
    f = open(input('path to keys: '), 'r')

    fw = open('new_image.png', 'r+b')
    img_code = str(fw.read())

    fl = open('code_img.txt', 'w')
    flw = fl.write(img_code)
    fl.flush()
    fl.close()

    y = str([line.strip() for line in f])

    for i in range(len(findall(r'\((\d+)\,', y))):
        keys.append((int(findall(r'\((\d+)\,', y)[i]), int(findall(r'\,\s(\d+)\)', y)[i])))
    for key in keys:
        a.append(pix[tuple(key)][0])
    return ''.join([chr(elem) for elem in a])


print("Your message: ", decrypt_your_message())
