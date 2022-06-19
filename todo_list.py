file = "todo.json"

def go_todo():
    print("Возможные действия: ")
    print("1. Добавить задачу")
    print("2. Вывести список задач")
    print("3. Выход")
    comand = input("Укажите номер действия: ")

    if comand == "1":
        name = input("Сформулируйте задачу: ")
        category = input("Добавьте категорию к задаче: ")
        time = input("Добавьте время к задаче: ")
        new_task = {'category': category, 'name': name, 'time': time}
        list_tasks.append(new_task)
        writer(file, list_tasks)
    elif comand == "2":
        for task in list_tasks:
            print("Задача: ", task["name"], " Категория: ", task["category"], " Дата: ", task["time"])
    elif comand == "3":
        print("Работа завершена.")
        return None

def writer(filename, numbers):
    import json
    try:
        with open(filename, 'w') as f_obj:
            json.dump(numbers, f_obj)
    except Exception as e:
        print(e)

def reader(filename):
    '''
    Чтение содержимого json файла
    '''
    import json
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
        return numbers
    except Exception as e:
        return e

list_tasks = reader(file)
go_todo()
