from logging import getLogger
import codecs
import json

# exercise 1
with open("text.txt", 'w', encoding='utf-8') as f_obj:
    content = 'some text'
    while content != '':
        content = input("Введите данные: ")
        f_obj.write(content + '\n')
    print("Данные записаны в файл")

# exercise 2
with open("random-text.txt", encoding='utf-8') as f_obj:
    lines = 0
    words_list = []
    words = []
    i = 0
    for line in f_obj:
        lines += 1
        line = line.split(' ')
        words_list.append(line)
    print(f"Количество строк в файле: {lines}")
    for el in words_list:
        words.append(int(len(el)))
    for el in words:
        while i < int(len(words)):
            print(f"Количество слов в {i + 1} строке - {words[i]}")
            i += 1

# exercise 3
logger = getLogger(__name__)

staff = {'Иванов': 15000,
         'Петров': 25000,
         'Васечкин': 10000,
         'Лукьянов': 40000,
         'Сидоров': 17000,
         'Лужин': 30000}

try:
    with open("staff.txt", 'w', encoding='utf-8') as f_obj:
        for surname, salary in staff.items():
            f_obj.write(surname + '—' + str(salary) + '\n')
except Exception:
    logger.error('Произошла ошибка записи!')

with open("staff.txt", 'r', encoding='utf-8') as f_obj:
    i = 1
    res = []
    j = 0
    summa = 0
    cnt = 0
    for line in f_obj:
        print(line, end='')
        employee = line.split('—')
        if int(employee[i]) <= 20000:
            res.append(employee[i-1])
        summa = summa + int(employee[i])
        cnt += 1
    print("Сотрудники с зарплатой, меньше 20 тыс:")
    for el in res:
        while j < int(len(res)):
           print(res[j])
           j += 1
    average = summa / cnt
    print("Среднее значение заработной платы - {0:.0f}".format(average))

# exercise 4
rus_num = ({'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'})
new_result = []

with open("numbers.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
         line = line.split('—')
         new_result.append(rus_num[line[0]] + '—' + line[1])

try:
    with open("numbers-rus.txt", 'w', encoding='utf-8') as f_obj:
            f_obj.writelines(new_result)
except Exception:
    logger.error('Произошла ошибка записи!')

# exercise 5
try:
    with open("summa.txt", 'w+', encoding='utf-8') as f_obj:
        list = input('Введите числа: ')
        f_obj.writelines(list)
        summa = list.split(' ')
        print("Сумма введеных чисел = ", sum(map(int, summa)))
except IOError:
    logger.error('Произошла ошибка записи!')
except ValueError:
    logger.error('Произошла ошибка ввода!')

# exercise 6
sub = {}
lec = 0
with codecs.open("subjects.txt", 'r', "utf-8") as f_obj:
    for line in f_obj:
        subject, lectures, practice, lab = line.split()
        subject = subject.replace(":", "")
        lectures = lectures.replace("(л)", "")
        lectures = lectures.replace("—", "0")
        practice = practice.replace("(пр)", "")
        practice = practice.replace("—", "0")
        lab = lab.replace("(лаб)", "")
        lab = lab.replace("—", "0")
        sub[subject] = int(lectures) + int(practice) + int(lab)
    print(sub)

# exercise 7
profit = {}
result = []
profit_all = 0
av_profit = 0
i = 0
average_profit = {}
with codecs.open("firms.txt", 'r', "utf-8") as f_obj:
    for line in f_obj:
        firm, opf, proceeds, costs = line.split()
        profit[firm] = int(proceeds) - int(costs)
        if profit[firm] > 0:
             profit_all = profit_all + profit[firm]
             i += 1
    if i != 0:
        av_profit = profit_all / i
    else:
      print("Все фирмы получили убытки")
    average_profit = {'average_profit': av_profit}
    result.append(profit)
    result.append(average_profit)
    # print(result)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)
    print(f"Создан data.json с данными {result}")