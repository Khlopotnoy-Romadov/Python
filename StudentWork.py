# coding:utf8

## Перед использованием функции необходимо открыть файл, а после её вызова закрыть
## иначе будут испорчены добавляемые данные (функцию find это не касается)

file1 = open('students.txt', 'r', encoding='utf-8')
file2 = open('newStudents.txt', 'w', encoding='utf-8')

students = file1.read().splitlines()
print(students)

def add(name, firstName):
    students.append(name+" "+firstName)
    students.sort()
    students_add = map(lambda name: name + '\n', students)
    file2.writelines(students_add)

def find(firstName,name = "Null"):
    sms = ""
    if name == "Null":
        sms = "Укажите имя"
        return sms
    for i in range(len(students)):
        if students[i] == name + " " + firstName:
            sms = "Студент находится в группе"
            return sms
    sms = "Студента нет в группе"
    return sms

def replace(name, firstName,newName = "Null",newFirstName = "Null"):
    sms = ""
    if find(firstName,name) == "Студента нет в группе":
        sms = "Студента нет в группе"
        return sms
    if newName == "Null":
        newName = name
    if newFirstName == "Null":
        newFirstName = firstName
    for i in range(len(students)):
        if students[i] == name + " " + firstName:
            students[i] = newName + " " + newFirstName
    students.sort()
    students_add = map(lambda name: name + '\n', students)
    file2.writelines(students_add)

def remove(firstName, name = "Null"):
    if name == "Null":
        print("Введите фамилию и имя")
        return False
    if name + " " + firstName in students:
        print(name + " " + firstName)
        students.remove(name + " " + firstName)
        students.sort()
        students_add = map(lambda name: name + '\n', students)
        file2.writelines(students_add)
        return True
    else:
        print("Студента нет в списке")


print(find("Узумаки", "Наруто"))
print(find("Ромадов"))

replace("Дима", "Ромадов", "Димончик", "Ромадов")
file2.close()

file2 = open('newStudents.txt', 'w', encoding='utf-8')
add("Джун", "Ли")
file2.close()

file2 = open('newStudents.txt', 'w', encoding='utf-8')
remove("Зелёный", "Арбуз")
file2.close()


file1.close()