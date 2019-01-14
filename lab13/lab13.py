# !/usr/bin/env python3
# -*- codding:utf-8 -*-


#  Реалізувати пять класів (базовий і 4 нащадки, що описують працівників ІТ підприємства: - з погодинною оплатою (один з
# нащадків), - з фіксованою ставкою (другий нащадок), погодинник оформлений як ФОП (третій нащадок) і самозайнята особа
# яка працює за цівільно-правовим договором оплата у відповідності до кількості рядків програмного коду написаного за
# місяць (четвертий нащадок). Описати в базовому класі абстрактні методи для обчислення середньомісячної зарабітньої
# плати та податків з неї (податок на доходи фізичних осіб (ПДФО), військовий збір (ВЗ), єдиний податок (ЄП), єдиний
# соціальний внесок (ЄСВ) і т. д.).

# - Для погодинників формула для розрахунку зарплати така: середньомісячна зарплата = 20.8 * 8 * погодинна ставка (або
# реально відпрацьовані години * погодинна ставка), податки: ПДФО 18%,  ВЗ 1.5%

# - Для працівників з фіксованою оплатою середньомісячна зарплата = фіксирована місячна ставка, податки: ПДФО 18% ,
# ВЗ 1.5% .

# - Для ФОП зарплата погодинка + 10% (можна зекономити на податках і заплатити людині більше),  податки: ЄП 5%, ЄСВ
# 704 грн. щомісяця

# - Для самозайнятої особи ціна за рядок * кількість рядків, податки: ПДФО 18%, ВЗ 1.5 %, ЄСВ 704 грн щомісяця

#  Уявімо, що людей що отримують зп в конверті або на лєву картку немає :)

#  Згенерувати випадковим чином перелік працівників підприємства. Впорядкувати всю послідовність робітників за
# зменшенням середньомісячного зарабітку. При співпадінні зп – впорядковувати дані за алфавітом по прізвищу. Вивести
# ідентифікаційний код робітника, прізвище, зп і сумарний податок для всіх елементів переліку.

#  Грошовою одиницею не переймайтесь, може бути ціле число без копійок. або флоат
# Абстрактний метод класу це метод реалізація для якого відсутня. Абстрактний метод підлягає визначенню в
# класах-спадкоємцях. Сорі, я забув про це сказати на занятті


import abc
import random


class Employee(abc.ABC):
    """ Create abstract methods like interfaces """

    @abc.abstractmethod
    def get_salary(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_physical_tax(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_military_tax(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_united_tax(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_social_tax(self) -> float:
        raise NotImplementedError


class HourlyEmployee(Employee):
    """ Calculate different taxes for hourly employee """

    def __init__(self, name: str, rate: float):
        self.name = name
        self.rate = rate

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        return 20.8 * 8 * self.rate

    def get_physical_tax(self) -> float:
        return self.get_salary() * 0.18

    def get_military_tax(self) -> float:
        return self.get_salary() * 0.015

    def get_united_tax(self) -> float:
        return 0

    def get_social_tax(self) -> float:
        return 0


class MonthlyEmployee(Employee):
    """ Calculate different taxes for monthly employee """

    def __init__(self, name: str, rate: float):
        self.name = name
        self.rate = rate

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        return self.rate

    def get_physical_tax(self) -> float:
        return self.get_salary() * 0.18

    def get_military_tax(self) -> float:
        return self.get_salary() * 0.015

    def get_united_tax(self) -> float:
        return 0

    def get_social_tax(self) -> float:
        return 0


class EntrepreneurEmployee(Employee):
    """Calculate different taxes for Entrepreneur"""

    def __init__(self, name: str, rate: float):
        self.name = name
        self.rate = rate
        self.social_tax = 704

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        return 20.8 * 8 * 1.1 * self.rate

    def get_physical_tax(self) -> float:
        return 0

    def get_military_tax(self) -> float:
        return 0

    def get_united_tax(self) -> float:
        return self.get_salary() * 0.05

    def get_social_tax(self) -> float:
        return self.social_tax


class FreelancerEmployee(Employee):
    """ Calculate different taxes for Freelancer """

    def __init__(self, name: str, rate: float, count_lines: int):
        self.name = name
        self.rate = rate
        self.count_lines = count_lines
        self.social_tax = 704

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        return self.rate * self.count_lines

    def get_physical_tax(self) -> float:
        return self.get_salary() * 0.18

    def get_military_tax(self) -> float:
        return self.get_salary() * 0.015

    def get_united_tax(self) -> float:
        return 0

    def get_social_tax(self) -> float:
        return self.social_tax


def input_data() -> list:
    names = ('Ivan', 'Andrei', 'Irina', 'Maria', 'Tara\'s', 'Nadia', 'Dasha')
    employees = []
    for _ in range(random.randint(5, 10)):
        name = random.choice(names)
        employees.append(random.choice([
            HourlyEmployee(name, random.randint(100, 1000)),
            MonthlyEmployee(name, random.randint(10000, 30000)),
            EntrepreneurEmployee(name, random.randint(100, 1000)),
            FreelancerEmployee(name, random.randint(30, 50), random.randint(100, 1000))]))
    return employees


def employee_sort(employees: list) -> list:
    return sorted(employees,
                  key=lambda e: (e.get_salary(), e.get_name()), reverse=True)


def output(employees: list) -> None:
    for employee in employees:
        print("ID: ", id(employee))
        print("Name: ", employee.get_name())
        print("Salary: ", employee.get_salary())
        full_tax = employee.get_military_tax() + employee.get_physical_tax() + employee.get_social_tax() + \
                   employee.get_united_tax()
        print("Full tax: ", full_tax)
        print("\n")


output(employee_sort(input_data()))
