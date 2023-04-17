import logger
import model
import view


def run():
    while True:
        mode = view.choose_mode()
        if mode == '1':
            notes = view.new_notes()
            logger.add_new(notes)
        elif mode == '2':
            notes = view.notes_to_s()
            base = logger.get_base()
            result = model.search_notes(base, notes)
            view.show_found(result)
        if mode == '0':
            exit(0)
