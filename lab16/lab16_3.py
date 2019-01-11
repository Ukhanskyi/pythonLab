#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Веб-скрапінг це процес автоматичного збору загально-доступної відкритої інформації із Всесвітньої павутини.
# У цьому завданні передбачено наступне:
# Створити програму для автоматизованого збору даних про навчальні заклади області. Обробити сторінку за посиланням
# https://if.isuo.org/authorities/schools-list/id/626 cформувати перелік посилань на школи (місто, район, і т. д. можна
# обрати будь-який). Автоматизовано ітерувати сторінки згідно цього переліку і видобути інформацію про назву школи,
# телефон, e-mail, прізвище директора, кількість учнів (можна додати поля на свій розсуд). Звернути увагу, що щодо
# e-mail застосовано нескладні механізми кодування для приховування від програмних роботів. Результат сформувати у
# вигляді стандартного csv файла. csv файл має містити header з назвами полів. Надсилати самі csv непотрібно. Детальніше
# про csv формат https://en.wikipedia.org/wiki/Comma-separated_values
# Отримати доступ до html коду сторінки з Python можна за допомогою модулів urllib або requests. Один з простих
# варіантів:
# from urllib.request import urlopen
# html = urlopen("http://pythonscraping.com/pages/page1.html")
# print(html.read())
# Проти BeautifulSoup нічого не маю :)


import csv
import re
import urllib.parse
import requests
from bs4 import BeautifulSoup


def value_filter(value: str) -> str:
    return value.replace("\'", '').replace("\"", '').replace("\n", ' ')


def pack_to_table_tuple(tr):
    return tr.select_one('th'), tr.select_one('td')


def table_tuple_text(x) -> tuple:
    if x[0] and x[1]:
        key = ' '.join(x[0].text.split())
        raw_value = ' '.join(x[1].text.split())
        value = raw_value if raw_value else '-'
        if key == 'E-mail:' and value != '-':
            value = re.findall("'<a.*>(.*)</a>'",
                               urllib.parse.unquote(x[1].select_one('a')['onclick']))[0]
        return_tuple = (key, value)
    else:
        return_tuple = None
    return return_tuple


class School:
    def __init__(self, name: str, phone: str, email: str, director_name: str,
                 students_number: str, link: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.director_name = director_name
        self.students_number = students_number
        self.link = link


class SchoolsScrapper:
    def __init__(self, base_url, query) -> None:
        self.base_url = base_url
        self.soup = BeautifulSoup(requests.get(base_url + query).content,
                                  'html.parser')

    def set_link(self, link):
        self.soup = BeautifulSoup(requests.get(link).content, 'html.parser')

    def get_schools(self) -> list:
        schools = []
        for a in self.find_links():
            link = self.updated_link(a)
            table_dict = self.table_dict()
            school = School(value_filter(table_dict['Скорочена:']),
                            value_filter(table_dict['Телефони:']),
                            value_filter(table_dict['E-mail:']),
                            value_filter(table_dict['Директор:']),
                            value_filter(table_dict['Кількість учнів:']),
                            value_filter(link))
            schools.append(school)
        return schools

    def table_dict(self):
        return dict(
            filter(lambda t: t is not None,
                   map(table_tuple_text,
                       map(pack_to_table_tuple, self.soup.select('table > tr'))))
        )

    def updated_link(self, a):
        link = self.base_url + a['href']
        self.set_link(link)
        return link

    def find_links(self):
        return self.soup.select('table > tr > td > a')


def main():
    base_url = "https://if.isuo.org/"
    school_id = "authorities/schools-list/id/620"
    schools = SchoolsScrapper(base_url, school_id).get_schools()
    with open("Bolehiv_schools.csv", 'w', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        for school in schools:
            csv_writer.writerow([
                school.name,
                school.phone,
                school.email,
                school.director_name,
                school.students_number,
                school.link
            ])


if __name__ == '__main__':
    main()
