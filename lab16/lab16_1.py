#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Веб-скрапінг це процес автоматичного збору загально-доступної відкритої інформації із Всесвітньої павутини. У цьому
# завданні передбачено наступне: Створити програму для автоматичного видобування інформації і створення переліку з 50
# учасників за посиланням http://www.codeabbey.com/index/user_ranking. Результат сформувати у вигляді стандартного csv
# файла. Передбачити наявність наступних полів: номер у рейтингу, username, rank, "enlightenment", кількість розв'язаних
# завдань. Надсилати самі csv непотрібно. Детальніше про csv формат https://en.wikipedia.org/wiki/Comma-separated_values
#    Отримати доступ до html коду сторінки з Python можна за допомогою модулів urllib або requests. Один з простих
# варіантів:
# from urllib.request import urlopen
# html = urlopen("http://pythonscraping.com/pages/page1.html")
# print(html.read())
# Проти BeautifulSoup нічого не маю :)


from bs4 import BeautifulSoup
import requests
import re


html = requests.get("http://www.codeabbey.com/index/user_ranking").content
soup = BeautifulSoup(html, 'html.parser')

table = soup.find_all('tr')

with open('rank.csv', 'w') as f:
    for row in table[2:]:
        result = row.get_text().split()
        result = [_.replace(',', '') for _ in result]
        result = ','.join(result)
        f.write(result + '\n')
