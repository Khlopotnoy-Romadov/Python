documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}
instruction = ""

def list_shelfs():
 all = []
 for i in directories.keys():
  all.append(i)
 return all

def shelf_search(number_doc):
 isOk = False
 s = 0;
 for i in directories:
  for j in range(len(directories[i])):
   if directories[i][j] == number_doc:
    s = str(i)
    isOk = True
 if isOk:
  return s
 else:
  return False

def list_documents():
 for i in documents:
  print("№: " + str(i['number']) + ", тип: " + str(i['type']) + ", владелец: " + str(i['name']) +
        ", полка хранения: " + shelf_search(str(i['number'])))

while instruction != 'q':
    instruction = input("Введите команду: ")
    if instruction == 'ad':
     n = input("Введите номер документа: ")
     t = input("Введите тип документа: ")
     v = input("Введите владельца документа: ")
     p = input("Введите полку хранения: ")
     isOk = False
     for i in directories:
      if i == p:
       isOk = True
     if isOk == True:
      documents.append({'type': t, 'number': n, 'name': v})
      directories[p].append(n)
      print("Документ добавлен. Текущий список документов: ")
      list_documents()
     else:
      print("Такой полки не существует. Добавьте полку командой ads")
      print("Текущий список документов: ")
      list_documents()

    if instruction == 'd':
     n = input("Введите номер документа: ")
     isOk = False
     for i in range(len(documents)):
      if documents[i]['number'] == n:
       del documents[i]
       isOk = True
       break
     if isOk == True:
      print("Документ удален.")
      print("Текущий список документов: ")
      list_documents()
     else:
      print("Документ не найден в базе.")
      print("Текущий список документов: ")
      list_documents()

    if instruction == 'm':
     n = input("Введите номер документа: ")
     isOk1 = False
     for i in documents:
      if i['number'] == n:
       isOk1 = True
     if isOk1 == False:
      print("Документ не найден в базе.")
      list_documents()
      break
     isOk2 = False
     s = input("Введите номер полки: ")
     for i in directories:
      if i == s:
       directories[i].append(n)
       isOk2 = True
     if isOk2 == False:
      print("Такой полки не существует. Текущий перечень полок: ", list_shelfs())
      break
     for j in directories[i]:
        if j == 'n':
         del directories[i][j]
     print("Документ перемещён. Текущий список документов: ")
     list_documents()


