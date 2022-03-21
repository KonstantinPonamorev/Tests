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

def delete_doc():
    doc_number = str(input('Введите номер документа: '))
    new_documents = [d for d in documents if str(d.get('number')) != doc_number]
    if len(new_documents) == len(documents):
        print('Такого документа нет')
    else:
        for directory in directories:
            if directory.

    print(new_documents)
    print(directories)
    return new_documents, directories

delete_doc()



def people_name():
    doc_number = input('Введите номер документа: ')
    count = 0
    for document in documents:
        if str(document["number"]) == str(doc_number):
            print(f'Человека с этим номером документа зовут {document["name"]}')
            count = 1
    if count != 1:
        print('Человека с таким номером документа нет в списке')


def shelf_number():
    doc_number = input('Введите номер документа: ')
    count = 0
    for i in range(1, len(directories) + 1):
        if doc_number in list(directories[str(i)]):
            print(f'документ на {i} полке')
            count = 1
    if count != 1:
        print('Документа нет на полках')


def doc_list():
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')


def add_doc():
    doc_type = input('Введите тип документа: ')
    doc_number = input('Введите номер документа: ')
    doc_name = input('Введите имя человека: ')
    shelf = input('На какую полку положить документ: ')
    doc = {}
    doc["type"] = doc_type
    doc["number"] = doc_number
    doc["name"] = doc_name
    documents.append(doc)
    if shelf in list(directories):
        directories[shelf].append(doc_number)
    else:
        print('Такой полки нет, документ пока в руках :)')
    print(documents)
    print(directories)
    return documents, directories


def command():
    command = input('Введите команду: ')
    if command == 'p':
        people_name()
    elif command == 's':
        shelf_number()
    elif command == 'l':
        doc_list()
    elif command == 'a':
        add_doc()
    else:
        print('Такой команды нет... Но скоро появится :)')


if __name__ = '__main__'
    print('Список комманд', 'p - поиск человек по номеру документа',
          's - узнать полку на которой лежит документ', 'l - список всех документов',
          'a - добавить новый документ и положить на полку', sep='\n'
          )
    command()
