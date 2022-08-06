# модуль поиска.

def search_data(word, data):
    if len(data) > 0:
        for i in data:
            # word = input('Введите фамилию для поиска: ')
            if word in i:
            #     print(data)
            # else:
            #     print('Сотрудников с такой фамилией нет!')
               return i