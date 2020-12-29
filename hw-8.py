from abc import ABC, abstractmethod
from datetime import datetime

# exercise 1
class Data:
    def __init__(self, dmy: str):
        self.dmy = dmy

    def new_form(self):
        list = self.dmy.split('-')
        return f'{list[0]} число, {list[1]} месяц, {list[2]} год'

    @staticmethod
    def validate(data):
        try:
            list = data.dmy.split('-')
            new_date = datetime(int(list[2]), int(list[1]), int(list[0]))
            print('Дата корректная')
        except Exception as err:
            print('Дата некорректная!', err)

data = Data("32-12-2020")
print(data.new_form())
Data.validate(data)

# exercise 2
class OwnError(Exception):
    def __init__(self, *args):
        self.text = args[0]

def division(a, b):
    if b == 0:
        raise OwnError("Деление на 0 невозможно.")
    return a / b

try:
    division(18, 0)
except Exception as err:
    print(type(err), err)

# exercise 3
class My_exception(ValueError):
    pass

def func():
    a = 1
    res = []
    while a == 1:
        number = input("Введите число или stop для выхода: ")
        if number == 'stop':
            a = 0
            break
        else:
            try:
                if not number.isdigit():
                    raise My_exception(number)
                res.append(int(number))
            except My_exception as err:
                print("Введено не число!", err)

    print("Список введеных чисел - ", res)

print(func())

# exercise 4
class Equipment(ABC):
    type: str
    id: int
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def arrival(self):
        pass


class Store:
    equipments = []
    cnt = 0

    def add_equipment(self, new_equip: Equipment):
        self.cnt += 1
        new_equip.id = self.cnt
        self.equipments.append(new_equip)

    def remove_equipment(self):
        for el in self.equipments:
            print(el.info())
        id_remove = int(input("Введите номер товара для отправки - "))
        for el in self.equipments:
            if el.id == id_remove:
                self.equipments.remove(el)
                print("Товар отправлен!")

    def menu(self):
        print("Для добавления принтера на склад - нажмите 1 \n" 
              "Для добавления сканера на склад - нажмите 2 \n"
              "Для добавления ксерокса на склад - нажмите 3 \n"
              "Для отправки товара со склада - нажмите 4 \n"
              "Для выхода из меню, нажмите 0 \n")
        a = 1
        while a == 1:
            choice = int(input("Введите цифру - "))
            if choice == 1:
                print("Добавление принтера на склад")
                new_printer = Printer()
                new_printer.arrival()
                self.add_equipment(new_printer)
            elif choice == 2:
                print("Добавление сканера на склад")
                new_scanner = Scanner()
                new_scanner.arrival()
                self.add_equipment(new_scanner)
            elif choice == 3:
                print("Добавление ксерокса на склад")
                new_xerox = Xerox()
                new_xerox.arrival()
                self.add_equipment(new_xerox)
            elif choice == 4:
                print("Отправка товара со склада")
                self.remove_equipment()
            elif choice == 0:
                a = 0
                break
            else:
                try:
                     if not choice.isdigit():
                        raise My_exception(choice)
                except My_exception as err:
                        print("Введено не число!", err)


class Printer(Equipment):
    type = 'printer'
    print_type: str
    cnt_cartridge: int
    print_format: str

    def info(self):
        return f"{self.id}. Принтер тип - {self.print_type}, кол-во картриджей - {self.cnt_cartridge}, формат печати - {self.print_format}"

    def arrival(self):
        try:
           self.print_type = input("Введите тип принтера - ")
           self.cnt_cartridge = int(input("Введите количество картриджей - "))
           self.print_format = input("Введите формат печати - ")
           print("Принтер добавлен!")
        except ValueError as err:
                print("Ошибка ввода!", err)


class Scanner(Equipment):
    type = 'scanner'
    resolution: str
    color_bit: int

    def info(self):
        return f"{self.id}. Сканер с разрешением - {self.resolution} и количеством цветов - {self.color_bit}"

    def arrival(self):
        try:
           self.resolution = input("Введите разрешение сканера - ")
           self.color_bit = int(input("Введите количество цветов - "))
           print("Сканер добавлен!")
        except ValueError as err:
                print("Ошибка ввода!", err)

class Xerox(Equipment):
    type = 'xerox'
    num_copies: int

    def info(self):
        return f"{self.id}. Ксерокс с максимальным количеством копий - {self.num_copies}"

    def arrival(self):
        try:
           self.num_copies = int(input("Введите количество копий - "))
           print("Ксерокс добавлен!")
        except ValueError as err:
                print("Ошибка ввода!", err)

store = Store()
Store.menu(store)


# exercise 7
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Комплексное число = {self.a} + {self.b}i"

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

complex_1 = Complex(2, 4)
complex_2 = Complex(6, 10)

complex_3 = complex_1 + complex_2
print(complex_3)

complex_4 = complex_1 * complex_2
print(complex_4)

