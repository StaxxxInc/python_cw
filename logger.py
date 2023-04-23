# Добавление
def write_data(data):
    with open('secret documents.csv', 'a', encoding="utf-8") as file:
        for i in data: file.write(i +' ')
        print("")

# Поиск    
def get_base():
    with open('notebook.csv', 'r', encoding='utf-8') as file:
        return file.read()

def search_note(base, note):
    base = base.split('\n')
    flag = True
    results = []
    for i in base:
        if note in i:
            flag = False
            results.append(i)
    if flag:
        results.append(f'заметка *{note}* не найдена')
    return results

# Результаты поиска
def search_result(result):
    print('Результаты поиска: ')
    for i in result:
        print(i)


# Удаление
def delete(base,s):
    base = base.split(" ")
    base.remove(s)
    return base

# Редактирование
def update(new_info):
    new_info_csv =[i.split(" ") for i in new_info]
    with open('secret documents.csv', 'w', encoding="utf-8") as f:
        writer = csv.writer(f,delimiter=" ")
        writer.writerows(new_info_csv)