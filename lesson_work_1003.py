#Задание 2

students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня": 10}
for x in students:
    if x in grades:
        print(grades[x])
    else:
        print("Контрольную работу не писал(а)")

print("------------")

for x in students:
    if x in grades and grades[x] >= 8:
        print(grades[x])

print("------------")

good = []
bad = []
for x in grades:
    if grades[x] > 5:
        good.append(x)
    else:
        bad.append(x)
print(good)
print(bad)

print("------------")

#Задание 3

marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}

def srzn(x: int):
    otvet = 0
    for i in marks:
        otvet += marks[i][x-1]
    return (otvet/len(marks))

print(srzn(2))

print("------------")

#Задание 4

marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}
categories = {'отлично' : [8, 9, 10],
             'хорошо' : [6, 7],
             'удовлетворительно' : [4, 5],
             'неуд' : [0, 1, 2, 3]}

def f(x: int):
    srzn = 0
    for i in marks:
        srzn += marks[i][x - 1]
    srzn = round(srzn/2)
    for i in categories:
        if srzn in categories[i]:
            return "Курс " + str(x) +  " " + i

print(f(2))

print("------------")

#Задание
marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}


def count_marks(mark: int):
    count = 0
    for i in marks:
        for j in marks[i]:
            if j >= mark:
                 count += 1
    return count
print(count_marks(6))

print("------------")

#Задание 34

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

mas = []
slova = 0
for x in queries:
    mas.append(len(x.split()))
mas_uniq = set(mas)
print(mas)
for i in mas_uniq:
    print("Поисковых запросов, содержащих " + str(i) + " слова(а): " +
          str(round(mas.count(i)/len(mas)*100,2)) + "%")

print("------------")

#Задание 35

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},}
for x in results:
    results[x]['ROI'] = round((results[x]['revenue']/results[x]['cost']-1)*100,2)
sorted_keys = sorted(results.keys())
sorted_results = {}
for i in sorted_keys:
    sorted_results[i] = results[i]
print(sorted_results)