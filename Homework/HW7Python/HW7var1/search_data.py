# Модуль поиска данных.

from import_data import import_data
from input_data import input_data

def search_data(word, data):
    if len(data) > 0:
        for i in data:
            if word in i:
                return i
    else:
        return None