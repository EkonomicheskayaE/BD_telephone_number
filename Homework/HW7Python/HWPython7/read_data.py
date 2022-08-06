# модуль чтения данных из файла.

# from tel_guide import tel_guide

# data = [input('Введите фамилию: '), input('Введите имя: '), input('Введите номер телефона: '), input('Введите дополнительную информацию: ')]
def read_data():
    with open('guide.csv', 'r', encoding='utf-8') as file:
        data = file.readline()
        list_of_rows = data.split()
    return list_of_rows
    
# read_data(data)




        
        