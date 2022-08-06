# Модуль удаления данных.

def del_data(data, num):
    if len(data) > 0:
        for i in data:
            if num in i:
                del num
    else:
        return None