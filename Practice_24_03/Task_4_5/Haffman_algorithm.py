def get_Haffman_codes(list_symbols):
    list_symbols = {key: value for key, value in sorted(list_symbols.items(), key=lambda x: -x[1])}
    result = dict([(x, "") for x in list(list_symbols.keys())])  # Создаем словарь для всех конечных кодов
    new_dict = list_symbols.copy()  # словарь в котором находится положение кодов в данный момент
    # Выполняем цикл до тех пор, пока не останется один ключ, содержащий все возможные значения
    while len(new_dict) != 1:
        for i in list(list_symbols.keys()):
            # Добавляем последним(менее встречающимся) двум элементам либо 0 либо 1 в начало,
            # тем самым строя в словаре result дерево кодов Хаффмана
            result[i] = "0" + result[i] if i in list(new_dict.keys())[-1] else \
                ("1" + result[i] if i in list(new_dict.keys())[-2] else result[i])
        # Создаем новый ключ содержащий предыдущие два со значением равным их сумме
        new_dict[":".join(list(new_dict.keys())[-2:])] = sum(list(new_dict.values())[-2:])
        # Удаляем те элементы, которые только что объеденили
        new_dict.pop(list(new_dict.keys())[-2])
        new_dict.pop(list(new_dict.keys())[-2])
        new_dict = {key: value for key, value in sorted(new_dict.items(), key=lambda x: -x[1])}
    return result


def adaptive_Haffman_code(string, alphabet):
    result = ""
    all_symbols = dict([(i, 1) for i in alphabet])  # Словарь - ключ -> символ : значение -> количество появлений
    end = False

    codes = get_Haffman_codes(all_symbols)  # С помощью обычного Хаффмана создаем
    # словарь кодов по частое появления символов в настоящий момент

    # Проходимся посимвольно по строке и добавляем в результат код для символа в данный момент
    for i in range(len(string)):
        result += codes[string[i]]
        all_symbols[string[i]] += 1
        codes = get_Haffman_codes(all_symbols)  # обновляем коды символов
    return result


def adaptive_Haffman_code_with_esc(string):
    result = ""
    all_symbols = dict(
        [(i, 1) for i in ["__NULL_ESC_SYMBOL__", "۞"]])  # Словарь - ключ -> символ : значение -> количество появлений
    end = False

    codes = get_Haffman_codes(all_symbols)  # С помощью обычного Хаффмана создаем
    # словарь кодов по частое появления символов в настоящий момент
    # Проходимся посимвольно по строке
    for i in range(len(string)):
        # Если символ уже встречался - добавляем одно появление по ключу и добавляем код в строку результата
        if string[i] in list(all_symbols.keys()):
            result += codes[string[i]]
            all_symbols[string[i]] += 1
        # Если символ встречается первый раз - добавляем символ ESC(чтобы показать декодеру,
        # что дальше идет код ASCII символа) +  код ASCII символа
        # Плюс добавляем в словарь символов со значением 1
        else:
            result += codes["__NULL_ESC_SYMBOL__"] + f"{ord(string[i]):08b}"
            all_symbols[string[i]] = 1
        codes = get_Haffman_codes(all_symbols)  # обновляем коды символов

    return result


def decoding_adaptive_Haffman_code(string, alphabet):
    result = ''
    i = 0
    all_symbols = dict([(i, 1) for i in alphabet])  # Словарь - ключ -> символ : значение -> количество появлений
    codes = get_Haffman_codes(all_symbols)  # С помощью обычного Хаффмана создаем
    # словарь кодов по частое появления символов в настоящий момент

    # Проходися по всей строке аналогично кодеру проделывая те же действия в обратной послед-ти.
    while i < len(string):
        for code in codes:
            if string[i:].find(codes[code]) == 0:
                result += code
                i += len(codes[code])
                all_symbols[code] += 1
                codes = get_Haffman_codes(all_symbols)  # обновляем коды символов

    return result


def decoding_adaptive_Haffman_code_with_esc(string):
    i = 0
    result = ""
    all_symbols = dict([(i, 1) for i in ["__NULL_ESC_SYMBOL__", "۞"]])

    codes = get_Haffman_codes(all_symbols)  # С помощью обычного Хаффмана создаем
    # словарь кодов по частое появления символов в настоящий момент

    # Проходися по всей строке аналогично кодеру проделывая те же действия в обратной послед-ти.
    while i < len(string):
        for code in codes:
            if string[i:].find(codes[code]) == 0:
                i += len(codes[code])
                # Если нет ESC значит символ уже в нашем алфавите => просто добавляем 1 к значению
                if code != "__NULL_ESC_SYMBOL__":
                    all_symbols[code] += 1
                    result += code
                # Иначе нужно считать ASCII код и добавить его символ в алфавит
                else:
                    all_symbols[chr(int(string[i: i + 8], 2))] = 1
                    result += chr(int(string[i: i + 8], 2))
                    i += 8
                codes = get_Haffman_codes(all_symbols)  # обновляем коды символов
    return result
