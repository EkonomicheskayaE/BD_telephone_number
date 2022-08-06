from output_data import output_data
from import_data import import_data
from input_data import input_data
from search_data import search_data
from del_data import del_data

def in_data():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    number_phone = input('Введите номер телефона: ')
    note = input('Введите описание: ')
    return [last_name, first_name, number_phone, note]

def choise_sep():
    mains = input('Введите разделитель: ')
    if mains == '':
        mains = None
    return mains

def choice_todo():
    print('Что хотите сделать?\n 1 - добавить контакт\n 2 - вывести данные из справочника\n 3 - найти контакт\n 4 - удалить контакт\n')
    operation = input('Введите цифру --> ')
    if operation == '1':
        mains = choise_sep()
        import_data(in_data(), mains)
    if operation == '2':
        data = output_data()
        input_data(data)
    if operation == '4':
        # delete = input('Кого вы хотите удалить? ')
        i = input_data()
        data = [i[0].center(10), i[1].center(10), i[2].center(15), i[3].center(10)]
        data.remove(input('Кого вы хотите удалить? '))
        
    if operation == '3':
        word = input('Введите данные для поиска: ')
        data = output_data()
        i = search_data(word, data)
        if i != None:
            print('Фамилия'.center(10), 'Имя'.center(10), 'Номер телефона'.center(15), 'Описание'.center(10),)
            print('*'*60)
            print(i[0].center(10), i[1].center(10), i[2].center(15), i[3].center(10))
        else:
            print('Данные не обнаружены!')