# exercise 1
list_1 = ['some text', 450, 3.78, False]
print(list_1, '-', type(list_1))
for x in list_1: print(x, '-', type(x))

# exercise 2
cnt = int(input("Сколько элементов в списке: "))
x = 0
list_result = []
while x < cnt:
    el = input(f"Введите {x} элемент списка - ")
    x += 1
    list_result.append(el)
print("Полученный список - ", list_result)

j = 0
for i in range(int(cnt / 2)):
         list_result[j], list_result[j+1] = list_result[j+1], list_result[j]
         j += 2
print("Список с перестановкой - ", list_result)

# exercise 3
mounth = input("Введите номер месяца: ")
# dict
dict_season = dict({'1': 'Winter',
                    '2': 'Winter',
                    '3': 'Spring',
                    '4': 'Spring',
                    '5': 'Spring',
                    '6': 'Summer',
                    '7': 'Summer',
                    '8': 'Summer',
                    '9': 'Autumn',
                    '10': 'Autumn',
                    '11': 'Autumn',
                    '12': 'Winter'})
print("It's a ", dict_season.get(mounth))

# list
mounth = int(input("Введите номер месяца: "))
list_season = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']
print("It's a ", list_season[mounth-1])

# exercise 4
text = input("Введите текст: ").split(" ")
for index, word in enumerate(text, 1):
    print(index, word[:10])

# exercise 5
rating = [8, 6, 3, 3, 1]
print("Текущий набор рейтинга: ", rating)
new = int(input("Введите новый элемент рейтинга: "))
rating.append(new)

# с while
list_len = len(rating)
i = list_len
while (rating[i-1] > rating[i-2]) and (i > 1):
     rating[i-1], rating[i-2] = rating[i-2], rating[i-1]
     i -= 1
print("С сортировкой while: ", rating)

# с функцией .sort
rating.sort(reverse = True)
print("С сортировкой .sort: ", rating)


