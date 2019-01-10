#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Створити консольну програму для керування телефонною книгою. Записи книги повинні містити імя абонента, прізвище і
# номер телефона. Забезпечити можливість додавання, перегляду і видалення записів, а також пошук за іменем або за
# номером телефону. Діалог із користувачем реалізувати у вигляді консольного меню (введіть 1 для додавання, 2 для
# видалення, і т. д.). Програма повинна зберігати дані на диск і читати їх при наступному запуску.


class PhoneBookMember():
    def __init__(self, name: str, fname: str, phone_number: str):
        self._name = name
        self._fname = fname
        self._phone_number = phone_number

    @property
    def get_name(self):
        return self._name

    @property
    def get_fname(self):
        return self._fname

    @property
    def get_number(self):
        return self._phone_number


class Model():
    def __init__(self):
        self.filename = 'phonebook.txt'

    def add_member(self, member) -> None:
        with open(self.filename, 'a') as f:
            data = member.name + ' ' + member.fname + '\n' + \
                   member.get_number + '\n'
            f.write(data)
            f.flush()

    def get_member(self, name: str, fname: str) -> PhoneBookMember:
        member = None
        with open(self.filename, 'r') as f:
            for line in f:
                if line == str(name) + ' ' + str(fname) + '\n':
                    phone_number = f.__next__()
                    phone_number = phone_number.replace('\n', '')
                    member = PhoneBookMember(name, fname, phone_number)
                    break
        return member

    def get_members(self) -> list:
        with open(self.filename, 'r') as f:
            is_name = True
            full_name = []
            for line in f:
                line = line.replace('\n', '')
                if is_name:
                    full_name = line.split(' ')
                    is_name = False
                else:
                    is_name = True
                    yield PhoneBookMember(full_name[0], full_name[1], line)

    def del_member(self, name: str, fname: str) -> None:
        lines = ''
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        with open(self.filename, 'w') as f:
            is_prev_deleted = False
            for line in lines:
                if is_prev_deleted:
                    is_prev_deleted = False
                    continue
                if line != str(name) + ' ' + str(fname) + '\n':
                    f.write(line)
                else:
                    is_prev_deleted = True


class View():
    def input_choice(self) -> int:
        welcome_text = "1.Add member\n2.Show member\n3.Show all\n" + \
                       "4.Delete member\n0.Quit"
        print(welcome_text)
        return int(input())

    def input_member(self) -> PhoneBookMember:
        name = input("Input member`s name: ")
        fname = input("Input member`s fname: ")
        phone_number = input("Input member`s phone number: ")
        return PhoneBookMember(name, fname, phone_number)

    def input_name(self) -> tuple:
        name = input("Input member`s name: ")
        fname = input("Input member`s fname: ")
        return (name, fname)

    def output_member(self, member) -> None:
        if member:
            print("Name:", member.name)
            print("FName:", member.fname)
            print("Phone number:", member.phone_number)
        else:
            print("Member not exists")

    def output_members(self, members: list) -> None:
        for member in members:
            self.output_member(member)
            print()


class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self) -> None:
        while (True):
            choice = self.view.input_choice()
            if choice == 0: break
            if choice == 1:
                self.model.add_member(self.view.input_member())
            elif choice == 2:
                member_name = self.view.input_name()
                self.view.output_member(self.model.get_member(
                    member_name[0], member_name[1]))
            elif choice == 3:
                self.view.output_members(self.model.get_members())
            elif choice == 4:
                member_name = self.view.input_name()
                self.model.del_member(member_name[0], member_name[1])
            else:
                raise ValueError("Incorrect choice")


def main():
    controller = Controller()
    controller.run()


main()
