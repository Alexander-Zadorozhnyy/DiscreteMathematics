def get_ShannonFano_codes(list_symbols, list_probability):
    # Условия выхода из рекурсии
    if len(list_symbols) == 1:
        return {list_symbols[0]: ""}
    if len(list_symbols) == 2:
        return {list_symbols[0]: "0", list_symbols[1]: "1"}

    result = dict([(x, "") for x in list_symbols])  # Создаем словарь для всех конечных кодов
    index = 2
    # Делим на две группы, чтобы разница между ними была минимальна
    while sum(list_probability[0:index]) < sum(list_probability[index:]) or abs(
            sum(list_probability[0:index - 1]) - sum(list_probability[index - 1:])) > \
            abs(sum(list_probability[0:index]) - sum(list_probability[index:])):
        index += 1

    # Дописываем 0 для всех кодов из первой группы, и 1 для всех кодов из второй группы.
    # Спускаемся по дереву до тех пор, пока не получим 1 или 2 элемента во всем словаре
    for k, v in get_ShannonFano_codes(list_symbols[:index - 1], list_probability[:index - 1]).items():
        result[k] = "0" + v
    for k, v in get_ShannonFano_codes(list_symbols[index - 1:], list_probability[index - 1:]).items():
        result[k] = "1" + v

    return result
