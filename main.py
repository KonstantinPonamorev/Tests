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



def people_name(doc_number):
    count = 0
    for document in documents:
        if str(document["number"]) == str(doc_number):
            result = f'Человека с этим номером документа зовут {document["name"]}'
            count = 1
    if count != 1:
        result = 'Человека с таким номером документа нет в списке'
    print(result)
    return count


def shelf_number(doc_number):
    count = 0
    for i in range(1, len(directories) + 1):
        if doc_number in list(directories[str(i)]):
            result = f'документ на {i} полке'
            count = 1
    if count != 1:
        result = 'Документа нет на полках'
    print(result)
    return count


def doc_list():
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')
    return documents


def add_doc(doc_type, doc_number, doc_name, shelf):
    doc = {}
    doc["type"] = doc_type
    doc["number"] = doc_number
    doc["name"] = doc_name
    documents.append(doc)
    if shelf in list(directories):
        directories[shelf].append(doc_number)
        marker = 1
    else:
        print('Такой полки нет, документ пока в руках :)')
        marker = 0
    print(documents)
    print(directories)
    return marker


def command():
    command = input('Введите команду: ')
    if command == 'p':
        doc_number = input('Введите номер документа: ')
        people_name(doc_number)
    elif command == 's':
        doc_number = input('Введите номер документа: ')
        shelf_number(doc_number)
    elif command == 'l':
        doc_list()
    elif command == 'a':
        doc_type = input('Введите тип документа: ')
        doc_number = input('Введите номер документа: ')
        doc_name = input('Введите имя человека: ')
        shelf = input('На какую полку положить документ: ')
        add_doc(doc_type, doc_number, doc_name, shelf)
    else:
        print('Такой команды нет... Но скоро появится :)')



if __name__ == '__main__':
    print('Список комманд', 'p - поиск человек по номеру документа',
          's - узнать полку на которой лежит документ', 'l - список всех документов',
          'a - добавить новый документ и положить на полку', sep='\n'
          )
    command()