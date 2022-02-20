print("Введите имя: ")
name = input()
if len(name) < 5:
    print("Введите фамилию: ")
    family = input()
    print((name+family).upper())
else:
    print(name.lower())