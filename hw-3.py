# exercise 1
def div_func ():
    var_1 = int(input("Введите первое число: "))
    var_2 = int(input("Введите второе число: "))
    try:
        result = (var_1 / var_2)
    except ZeroDivisionError:
        print("You cannot divide by zero!")
        return
    return result

print("Результат деления: ", div_func())

# exercise 2
name_src = input("Введите имя: ")
surname_src = input("Введите фамилию: ")
year_src = input("Введите год рождения: ")
city_src = input("Введите город проживания: ")
email_src = input("Введите email-адрес: ")
phone_src = input("Введите телефон: ")

dict_params = dict({'name': name_src,
                    'surname': surname_src,
                    'year': year_src,
                    'city': city_src,
                    'email': email_src,
                    'phone': phone_src
})

def user_inf (name, year, surname, city, email, phone):
 print(f"Hi, {name} {surname}, you were born in {year} and you from {city}, your email is {email}, phone  - {phone}")

user_inf(**dict_params)

# exercise 3
a = int(input("Введите 1-ый аргумент: "))
b = int(input("Введите 2-ой аргумент: "))
c = int(input("Введите 3-ий аргумент: "))

def my_func(arg_1, arg_2, arg_3):
    mn = arg_1
    if arg_2 < mn: mn = arg_2
    if arg_3 < mn: mn = arg_3
    return arg_1 + arg_2 + arg_3 - mn

print("Сумма двух наибольших = ", my_func(a, b, c))

# exercise 4
var_1 = int(input("Введите число x: "))
var_2 = float(input("Введите число y: "))

# с использование оператора **
def my_func1(x, y):
    return x ** y
print("x в степени у = ", my_func1(var_1,var_2))

# с использованием while
def exponentiation(x, y):
    i = 1
    res = 1
    if y < 0:
       while i <= (y * (-1)):
          res *= x
          i += 1
       return 1 / res
    else:
       while i <= y:
           res *= x
           i += 1
       return res

print("x в степени у = ", exponentiation(var_1, var_2))

# exercise 5
def my_func2():
    a = 1
    res = 0
    while a == 1:
        numbers = list(input("Введите строку чисел или q для выхода: ").split(" "))
        result = 0
        for el in range(len(numbers)):
            if numbers[el] == 'q':
                a = 0
                break
            else:
                try:
                   result = result + int(numbers[el])
                except ValueError:
                   print("Value Error")
        res = res + result
        print("Сумма введенных чисел =  ", res)
    print("Итоговая сумма всех введенных чисел =  ", res)

print(my_func2())

# exercise 6
word = input("Введите слово: ")

def int_func(word):
    return word.capitalize()

print(int_func(word))

words = list(input("Введите слова: ").split(" "))

for el in range(len(words)):
   words[el] = int_func(words[el])

word_cup = " ".join(words)
print(word_cup)










