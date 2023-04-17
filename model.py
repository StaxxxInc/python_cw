def search_notes(base, notes):
    base = base.split('\n')
    flag = True
    results = []
    for i in base:
        if notes in i:
            flag = False
            results.append(i)
    if flag:
        results.append(f'Заметка |{notes}| не найдена')
    return results