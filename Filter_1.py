documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people():
    command = input('Введите номер: ')
    for docs in documents:
        if command in docs['number']:
            return f"{command} - {docs['name']}"


def shelf():
    command = input('Введите номер: ')
    for key, val in directories.items():
        if command in val:
            return f"{command} - {key}-я полка"


def total_list():
    for docs in documents:
        print(f'{docs["type"]} "{docs["number"]}" "{docs["name"]}"')
    return f'Полный список данных'


def add_document():
    new_dict = dict(type=input('Введите "type":'),
                    number=input('Укажите "number":'),
                    name=input('Укажите "name": '))

    add_directories = input('Укажите полку:')
    if add_directories in directories:
        directories[add_directories].append(new_dict['number'])
        documents.append(new_dict)
    else:
        print('')
        print('Укажите номер полки от 1 до 3!')
        print('Введите данные еще раз')
        add_document()
    return documents, directories



def elem_delette():
    num = input('Укажите номер документа,которые хотите удалить:')
    for doc in documents:
        if num == doc['number']:
            doc.clear()
            for key, val in directories.items():
                if num in val:
                    val.remove(num)
                    print('Операция УСПЕШНА!')
        else:
          print('Документа с таким номером нет в базе!')
    return documents, directories



def move_docoment():
    number = input('Укажите "number":')
    move_directories = input('Укажите полку в которую переместить документ:')
    result = []
    for key in directories:
        for val in directories[key]:
            result.append(val)
    if move_directories in directories and number in result:
        for key in directories:
            if number in directories[key]:
                directories[key].remove(number)
                directories[move_directories].append(number)
    else:
        print('Такой полки или номера не сущевствует')
    print(result)
    return directories


def add_shelf():
  new_shelf = input('Введите номер новой полки: ')
  if new_shelf not in directories:
    directories[new_shelf] = []
  else:
      print('Полка с таким номером уже сущевствует!')
  return directories



def manager():
  """
  Список Общих команд:
  p - команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
  s - команда, которая спросит номер документа и выведет номер полки, на которой он находится;
  l - команда, которая выведет список всех документов;
  a - команда, которая добавит новый документ в каталог и в перечень полок;
  d - команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
  m - команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
  as - команда, которая спросит номер новой полки и добавит ее в перечень;
  """


  while True:
    print('')
    command = input('Введите Общую команду: ')
    if command == 'p':
      print(people())
    elif command == 's':
      print(shelf())
    elif command == 'l':
      print(total_list())
    elif command == 'a':
      print(add_document())
      print(documents)
      print(directories)
    elif command == 'd':
      print(elem_delette())
      print(documents)
      print(directories)
    elif command == 'm':
      print(move_docoment())
      print(documents)
      print(directories)
    elif command == 'as':
      print(add_shelf())
      print(documents)
      print(directories)
    elif command == 'q':
      break
    else:
      print('Такой команды не сущувствует.')

help(manager)
manager()