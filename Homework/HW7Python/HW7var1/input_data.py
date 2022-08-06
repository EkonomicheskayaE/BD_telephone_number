# Модуль ввода данных.

def input_data(data):
    if len(data) > 0:
        print('Фамилия'.center(10), 'Имя'.center(10), 'Номер телефона'.center(15), 'Описание'.center(10),)
        print('*'*60)
        for i in data:
            print(i[0].center(10), i[1].center(10), i[2].center(15), i[3].center(10))     
    else:
        print('Справочник пуст!')