# Модуль записи данных.

def import_data(data, means = None):
    with open('phone.csv', 'a') as file:
        if means == None:
            for i in data:
                file.write(f'{i}\n')
            file.write(f'\n')
        else:
            file.write(means.join(data))
            file.write(f'\n')