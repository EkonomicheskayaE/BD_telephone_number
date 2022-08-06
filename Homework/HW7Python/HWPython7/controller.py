from tel_guide import tel_guide
from read_data import read_data
from write_data import write_data
from search_data import search_data

def input_data():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    number_phone = input('Введите номер телефона: ')
    information = input('Введите дополнительную информацию: ')
    return surname, name, number_phone, information

def choise_sep():
    sep = input('Введите разделитель: ')
    if sep == '':
        sep = None
    return sep

def do_choice():
    print('Какое действие вы хотите сделать?\n\
    1 - добавить сотрудника\n\
    2 - посмотреть весь список сотрудников\n\
    3 - найти сотрудника')

    choise = input('Введите цифру нужного действия --> ')
    if choise == '1':
        sep = choise_sep()
        write_data(input_data())
    elif choise == '2':
        data = read_data()
        tel_guide(data)
    elif choise == '3':
        word = input('Введите фамилию сотрудника для поиска --> ')
        data = read_data()
        i = search_data(word, data)
        if i != None:
            print(i)
        else:
            print('Таких сотрудников нет!')
