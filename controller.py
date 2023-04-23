import function as f
import ui


def run():
    input_from_user = ''
    while input_from_user != '7':
        ui.menu()
        input_from_user = input().strip()
        #вывод всех заметок из файла
        if input_from_user == '1':
            f.show('all')
        #добавление заметки
        if input_from_user == '2':
            f.add()
        #удаление заметки
        if input_from_user == '3':
            f.show('all')
            f.id_edit_del_show('del')
        #редактирование заметки
        if input_from_user == '4':
            f.show('all')
            f.id_edit_del_show('edit')
        #выборка заметок по дате
        if input_from_user == '5':
            f.show('date')
        #показать заметку по id
        if input_from_user == '6':
            f.show('id')
            f.id_edit_del_show('show')
        #выход
        if input_from_user == '7':
            ui.exit()
            break
