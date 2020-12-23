# exercise 1
class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        res = []
        num = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                num.append(summa)
                if len(num) == len(self.matrix):
                    res.append(num)
                    num = []
        return Matrix(res)

m = Matrix([
    [1, 3, 4],
    [4, 6, 4],
    [4, 8, 2]
])
m2 = Matrix([
    [0, 4, 2],
    [1, 1, 3],
    [2, 9, 0]
])
print(m + m2 + m)

# exercise 2
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def rate(self):
        pass

    def __add__(self, other):
        return self.rate() + other.rate()


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def rate(self):
        return (self.size / 6.5 + 0.5)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == 'пальто':
            self.__name = 'Пальто'
        else:
            self.__name = name

    def get_name(self):
        return f"В заказ поступило изготовление типа - {str(self.name)}"


class Suit(Clothes):
    def __init__(self, name, growth):
        super().__init__(name)
        self.growth = growth

    def rate(self):
        return (2 * self.growth + 0.3)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == 'костюм':
            self.__name = 'Костюм'
        else:
            self.__name = name

    def get_name(self):
        return f"В заказ поступило изготовление типа - {str(self.name)}"


coat = Coat('пальто', 44)
print(coat.get_name())
print(f'Расход ткани для пальто, м - ', round(coat.rate(), 2))
suit = Suit('костюм', 52)
print(suit.get_name())
print(f'Расход ткани для костюма, м - ', round(suit.rate(), 2))
print(f'Расход ткани для всего, м - ', round(coat + suit, 2))

# exercise 3
class Cell:
    def __init__(self, number: int):
        self.number = number

    def __str__(self):
        return f'Количество клеток = {self.number}'

    def __add__(self, other):
        num = self.number + other.number
        return Cell(num)

    def __sub__(self, other):

        if self.number > other.number:
            num = self.number - other.number
        else:
            print('Вычитание не возможно')
        return Cell(num)

    def __mul__(self, other):
        num = self.number * other.number
        return Cell(num)

    def __truediv__(self, other):
        num = self.number // other.number
        return Cell(num)

    def make_order(self, instance, num_row):
        row = int(instance.number / num_row)
        ost = instance.number % num_row
        line = ''
        for i in range(row):
            line += f'{"*" * num_row}\\n'
        line += f'{"*" * ost}'
        return line

cell_1 = Cell(13)
cell_2 = Cell(27)
cell_3 = cell_1 + cell_2 + cell_1
print(cell_3)
cell_4 = cell_2 - cell_1
print(cell_4)
cell_5 = cell_1 * cell_2
print(cell_5)
cell_6 = cell_2 / cell_1
print(cell_6)

print(cell_1.make_order(cell_1, 5))

