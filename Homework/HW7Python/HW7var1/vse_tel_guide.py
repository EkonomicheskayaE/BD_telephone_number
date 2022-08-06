# вариант 1.

# data = {
#     'Фамилия': input('Введите фамилию: '),
#     'Имя': input('Введите имя: '),
#     'Телефон': input('Введите номер телефона: '),
#     'Доп. инфо': input('Введите дополнительную информацию: ')
#         }
# print(data['Фамилия'], data['Имя'], data['Телефон'], data['Доп. инфо'])

# вариант 2.

data = [input('Введите фамилию: '), input('Введите имя: '), input('Введите номер телефона: '), input('Введите дополнительную информацию: ')]
print(data)

# запись в файл

# with open('guide.csv', 'a', encoding="utf8") as file:
#     # for i in data:
#         # writer = csv.writer(file)
#         file.write(f'{data} \n')
       
        # file.write(f'\n') #если добавить эту команду, то запись (фамилия, имя и т д) будут с новой строки

# чтение из файла.
# with open('guide.csv', 'r', encoding='utf-8') as file:
#     a = file.read()
#     print(f'{a} \n')

# поиск.

# if len(data) > 0:
#     for i in data:
#         word = input('Введите фамилию для поиска: ')
#         if word in i:
#             print(data)
#         else:
#             print('Сотрудников с такой фамилией нет!')
# else:
#     None # не получается закончить цикл

# удаление из файла.

del data()







       

