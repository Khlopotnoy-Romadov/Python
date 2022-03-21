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

def list_documents():
 for i in documents:
  print("№: " + str(i['number']) + ", тип: " + str(i['type']) + ", владелец: " + str(i['name']) +
        ", полка хранения: " + shelf_search(str(i['number'])))

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


while instruction != 'q':
 instruction = input("Введите команду: ")


 if instruction == "p":
  number_doc = input("Введите номер документа: ")
  isOk = False;
  for i in range(len(documents)):
    if documents[i]['number'] == number_doc:
     print("Владелец документа: " + str(documents[i]['name']))
     isOk = True;
  if isOk == False:
     print("Документ не найден в базе")


 if instruction == "s":

  number_doc = input('Введите номер документа: ')
  if shelf(number_doc) == False:
   print("Документ не найден в базе")
  else:
   print("Документ хранится на полке: " + shelf_search(number_doc))



 if instruction == "l":
  list_documents()

 if instruction == "ads":
  shelf = input("Введите номер полки: ")
  all = []
  for i in directories.keys():
   all.append(i)
  isOk = True
  for x in directories:
   if x == shelf:
    isOk = False
    print("Такая полка уже существует. Текущий перечень полок: ", all)
  if isOk == True:
   all.append(shelf)
   directories[shelf] = []
   print("Полка добавлена. Текущий перечень полок: ", all)


 if instruction == "ds":
  shelf = input("Введите номер полки: ")
  all = []
  for i in directories.keys():
   all.append(i)
  isOk = True
  for x in directories:
   if x == shelf:
    isOk = False
    if directories[x] == []:
     del directories[x]
     all.remove(shelf)
     print("Полка удалена. Текущий перечень полок: ", all)
     break
    else:
     print("На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: ", all)
     break
  if isOk == True:
   print("Такой полки не существует. Текущий перечень полок: ", all)
print("Работа завершена")

