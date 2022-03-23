from decimal import Decimal
from decimal import getcontext


def get_arithmetic_coding_code(string, all_symbols):
    print(len(string))
    all_symbols = dict([(i, Decimal(str(all_symbols[i]))) for i in all_symbols.keys()])
    # задаем нужное количество знаков после запятой, для сохранения точностиa
    getcontext().prec = 2**32
    result = (Decimal("0"), Decimal("1"))
    segments_dict = dict()
    sum = Decimal("0")
    # Создаем список сегметнов, на которые разделен отрезок (0, 1)
    for i in range(len(list(all_symbols.keys()))):
        segments_dict[list(all_symbols.keys())[i]] = (sum, sum + list(all_symbols.values())[i])
        sum += list(all_symbols.values())[i]

    # Переходим в нужную часть выбранного в данный момент отрезка, относительно его концов.
    for i in string.replace("<EOF>", ""):
        result = (result[0] + (result[1] - result[0]) * segments_dict[i][0],
                  result[1] - (result[1] - result[0]) * (1 - segments_dict[i][1]))
    result = (result[0] + (result[1] - result[0]) * segments_dict["<EOF>"][0],
              result[1] - (result[1] - result[0]) * (1 - segments_dict["<EOF>"][1])) if "<EOF>" in string else result
    # Возвращаем координату начальной вершины, так как в качестве ответа можно
    # взять любую точку из полученного полинтервала
    return result[0]


# Перевод двоичного нецелого в Decimal - для большей точности
def bin_to_decimal(binary):
    res = 0
    for i in range(len(str(binary)) - 2):
        res += int(str(binary)[i + 2]) * 2 ** (-i - 1)
    return Decimal(str(res))


def decode_arithmetic_coding_code(answer, all_symbols):
    all_symbols = dict([(i, Decimal(str(all_symbols[i]))) for i in all_symbols.keys()])
    start = (Decimal("0"), Decimal("1"))
    result = ""
    segments_dict = dict()
    sum = Decimal("0")
    # Делим отрезок (0, 1) на части, относительно их вероятностей,
    # отступая от кажого следующего на вероятность настоящео
    for i in range(0, len(list(all_symbols.keys()))):
        segments_dict[list(all_symbols.keys())[i]] = (sum, sum + list(all_symbols.values())[i])
        sum += list(all_symbols.values())[i]
    # Перемещаемя по отрезкам, пока не найдем достаточно точный отрезок, в котором находится ответ
    while "<EOF>" not in result:
        for i in list(all_symbols.keys()):
            # Вычисляем нужный отрезок относительно локального отрезка, аналогично (0, 1)
            coords = (start[0] + (start[1] - start[0]) * segments_dict[i][0],
                      start[1] - (start[1] - start[0]) * (1 - segments_dict[i][1]))
            # Выбираем необходимую часть отрезка, в котором находится ответ
            if coords[0] <= answer < coords[1]:
                start = coords
                result += i
                break
    return result
