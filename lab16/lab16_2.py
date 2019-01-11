#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Створити скрипт який буде витягувати інформацію про ноутбуки з сайту http://price.ua/catc839t14.html. Поля які
# потрібно витягнути: назва, ціна, опис, посилання, посилання на фото. Вибрати тільки ноутбуки ціною від 10 до 20 тис.
# гривень. Результат зберігти в базу даних cvs файл. Створити UI на базі будь-якого веб-фреймворка.


import bs4
import requests
import csv
import re


def value_filter(value: str) -> str:
    return value.replace("\'", '').replace("\"", '').replace("\n", ' ')


def write_parsed_page(response, writer) -> None:
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    notebooks = soup.find_all(class_='product-block')

    for notebook in notebooks:
        name = notebook.find(class_='model-name').text
        price = notebook.find(class_='price').text
        all_desc = notebook.find_all(class_='short-descr-line')
        desc = '\n'.join([desc.text.strip() for desc in all_desc])
        link = notebook.find(class_='btn')['href']
        if link[0] == '/':
            link = "https://price.ua" + link
        photo_link = notebook.find(class_='photo-wrap').find('img')['src']
        photo_link = f"https:{photo_link}"
        writer.writerow([value_filter(name),
                         value_filter(price),
                         value_filter(desc),
                         value_filter(link),
                         value_filter(photo_link)])


url = "https://price.ua/catc839t14/page{}.html?price[min]=10000&price[max]=20000"
i = 1

with open("laptops.csv", 'w', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    while True:
        r = requests.get(url=url.format(i))
        page = int(re.search(r'page\d+', r.url).group(0).replace('page', '')) \
            if i != 1 else 1
        if i != page:
            break
        else:
            write_parsed_page(r, csv_writer)
            i += 1
