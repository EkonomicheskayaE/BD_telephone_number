# модуль записи данных.

def write_data(data):
    with open('guide.csv', 'a', encoding="utf8") as file:
        file.write(f'{data} \n')
        