# exercise 1
name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
gender = input("Введите ваш пол: ")
size = input("Введите ваш размер одежды: ")

print(f"Привет, {name}. Тебе {age}. Ты {gender}. И твой размер одежды {size}.")

# exercise 2
sec = int(input("Введите время в секундах: "))
hour = (sec / 3600) % 24
minute = (sec / 60) % 60
second = (sec % 60)

print("Время в часах, минутах и секундах: %02d:%02d:%02d" % (hour, minute, second))

# exercise 3
num = input("Введите число x: ")
n = len(num)
factor = 10**(2 * n) + 2 * (10**n) + 3
summa = factor * int(num)

print("Cумма в виде x+xx+xxx: ", summa)

# exercise 4
number = int(input("Введите число целое положительное число: "))
i = 0
if number < 10:
    i = number
while number > 10:
    d = number % 10
    number = number // 10
    if d > i:
        i = d

print("Наибольшая цифра в числе: ", i)

# exercise 5
proceeds = int(input("Введите выручку, руб: "))
costs = int(input("Введите издержки, руб: "))
result = (proceeds - costs)
profit = (result / proceeds)

if result > 0:
    print("Выручка больше издержек")
    print("Рентабельность - {0:.0f}%".format(profit * 100))
    employees = int(input("Введите кол-во сотрудников: "))
    result_per = (result / employees)
    print("Прибыль на одного сотрудника, руб: %.0f" % result_per)
else:
    print("Издержки больше выручки")

# exercise 6
a = int(input("Введите результат 1-го дня, км: "))
b = int(input("Какой результат вычислить, км: "))
i = 1
while a < b:
    a = a + a * 0.1
    i += 1

print("Спортсмен достигнет результата на", i, "день.")
