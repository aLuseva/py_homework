from sys import argv
from itertools import count
from functools import reduce
from itertools import cycle
from time import sleep

# exercise 1
def zp_func(work_hour, rate, award):
    return work_hour * rate + award

file_path, work_hour, rate, award = argv

try:
    work_hour = int(work_hour)
    rate = int(rate)
    award = int(award)
except ValueError as err:
    print(f"Ошибка ввода {err}")
print("Заработная плата сотрудника = ", zp_func(work_hour, rate, award))

# exercise 2
# c геренатором
my_list = [153, 1, 14, 41, 1, 1, 4, 15, 70, 1, 78, 99, 5]
r_list = [el for el in my_list if my_list.index(el) != 0 and el > my_list[my_list.index(el)-1]]
print(f"Исходный список: {my_list}")
print(f"Измененный список: {r_list}")

# c for
new_list = []
for i in range(len(my_list) - 1):
    if my_list[i] < my_list[i+1]:
        new_list.append(my_list[i+1])
        i += 1

print(f"Исходный список: {my_list}")
print(f"Измененный список: {new_list}")

# exercise 3
r_list = [x for x in range(20, 240) if x % 20 == 0 or x % 21 == 0]
print(f"Числа, кратные 20 или 21: {r_list}")

# exercise 4
orig_list = [1, 3, 4, 7, 23, 23, 44, 41, 3, 2, 10, 7, 4, 12, 18]
new_list = [el for el in orig_list if orig_list.count(el) == 1]
print(f"Элементы списка, не имеющие повторений: {new_list}")

# exercise 5
def my_func (prev_el, el):
    return prev_el * el

range_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f"Сгенерированный список: {range_list}")
print("Произведение всех элементов списка = ", reduce(my_func, range_list))

# exercise 6
'''Итератор, генерирующий целые числа, начиная с указанного'''
x = int(input("Введите стартовое число: "))
y = int(input("Введите конечное число: "))

for el in count(x):
    if el > y:
        break
    else:
        print(el)

'''Итератор, повторяющий элементы некоторого списка, определенного заранее'''
list = ['One', 'Two', 'Three', 'Four', 'Five']
i = 0
for el in cycle(list):
    if i > 9:
        break
    print(el)
    sleep(1)
    i += 1

# exercise 7
n = int(input("Введите число: "))

def fact(n):
    x = 1
    while x <= n:
         yield x
         x += 1

p = fact(n)

for el in fact(n):
    print(next(p))