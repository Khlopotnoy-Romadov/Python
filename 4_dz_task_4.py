#Задание 11

text = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

lst = text.split("\n")
lst_new = [x.split(" ") for x in lst]
otvet = []
pr = []
for item in lst_new:
    if len(pr) > 0:
        otvet.append(pr)
    pr = []
    for i in range(len(item)):
        if len(item[i]) > 3:
            pr.append(item[i])
print(otvet)