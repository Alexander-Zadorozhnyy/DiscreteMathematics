import math


# Считаем энтропию по формуле
def get_total_entropy_of_codes(list_of_probabalities):
    return -sum([i * math.log(i, 2) for i in list_of_probabalities])


# Считаем длину по формуле
def get_average_lenght(list_of_probabalities, list_of_codes):
    return sum(list_of_probabalities[i] * len(list_of_codes[i]) for i in range(len(list_of_codes)))


# Считаем избыточность по формуле
def get_message_redundancy(list_of_probabalities, list_of_codes):
    return 1 - get_total_entropy_of_codes(list_of_probabalities) / get_average_lenght(list_of_probabalities,
                                                                                      list_of_codes)


# Создаем словарь: ключ -> символ : значение -> кол-во появлений в строке
def get_dict_of_symbols(string, alphabet):
    all_symbols, count = dict.fromkeys(alphabet, 0), 0
    for x in alphabet:
        all_symbols[x] = string.count(x)
        count += string.count(x)
    # Сортируем словарь по возрастанию кол-ва появлений в строке
    all_symbols = {key: value for key, value in sorted(all_symbols.items(), key=lambda x: -x[1])}
    return all_symbols, count


# Создаем словарь из всевозможно встречающихся по n символов сочетаний
def make_alphabet(string, n):
    alphabet = ["<EOF>"] if "<EOF>" in string else []
    string = string.replace("<EOF>", "")

    for i in range(0, len(string) - 1, n):
        if string[i:i + n] not in alphabet:
            alphabet.append(string[i:i + n])

    return alphabet


def coding(string, codes):
    res = ''
    end = False
    # Проверяем есть ли символ <EOF> в строке, чтобы убрать его и в конце приписать его,
    # так как алгоритм работает посимвольно
    if "<EOF>" in string:
        end = True
        string = string.replace("<EOF>", "")

    # Посимвольно кодируем каждую букву
    for symbol in string:
        res += codes[symbol]

    return res + codes["<EOF>"] if end else res


def decoding(string, codes):
    res = ''
    i = 0
    # Перебираем все коды, приписываем с которого начинается строка
    while i < len(string):
        for code in codes:
            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])

    return res
