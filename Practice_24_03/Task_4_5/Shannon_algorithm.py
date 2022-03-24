import math


# Перевод нецелого числа к двоичному виду, так как базовый функционал не дает такой возможности
def float_to_bin(num):
    exponent = 0
    shifted_num = num
    while shifted_num != int(shifted_num):
        shifted_num *= 2
        exponent += 1
    if exponent == 0:
        return '{0:0b}'.format(int(shifted_num))
    binary = '{0:0{1}b}'.format(int(shifted_num), exponent + 1)
    integer_part = binary[:-exponent]
    fractional_part = binary[-exponent:].rstrip('0')
    return '{0}.{1}'.format(integer_part, fractional_part)


def get_Shannon_codes(list_symbols, list_probability):
    # L_list -> length of x symbol
    L_list = [math.ceil(-math.log(list_probability[i], 2)) for i in range(len(list_symbols))]
    # B_list -> bin(sum of probabilities before x.probability)
    B_list = ["0" * (2 + min(L_list))]
    sum = list_probability[0]
    for i in range(1, len(list_symbols)):
        B_list.append(float_to_bin(float(sum)))
        sum += list_probability[i]
    # Возвращаем словарь - ключ -> символ : значение -> код состоящий из L_list[х] знаков после запятой
    return dict([(list_symbols[i], B_list[i][2:L_list[i] + 2]) for i in range(len(list_symbols))])
