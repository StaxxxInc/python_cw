import csv

def add_new(contact):
    try:
         with open('notebook.csv', 'a') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([contact.split(' || ')])
    except FileNotFoundError:
         with open('notebook.csv', 'w') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([contact.split(' || ')])

def get_base():
    with open('notebook.csv', 'r', encoding='utf-8') as book:
        return book.read()
        
