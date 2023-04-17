from datetime import datetime

def notes_to_s():
    return input('Введите информацию для поиска: ')

def choose_mode():
    return input('Введите режим работ (1 - добавление, 2 - поиск, 0 - выход): ')

def new_notes():
    id = input('Введите идентификатор: ')
    header = input('Введите заголовок : ')
    note = input('Введите заметку: ')
    time = datetime.now()
 

    return f'{id} || {header} || {note} || {time}'

def show_found(result):
    print('Результат поиска: ')
    for i in result:
        print(i)