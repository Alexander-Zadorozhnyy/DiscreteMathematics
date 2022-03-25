from Haffman_algorithm import get_Haffman_codes, adaptive_Haffman_code, decoding_adaptive_Haffman_code, \
    adaptive_Haffman_code_with_esc, decoding_adaptive_Haffman_code_with_esc
from Shannon_algorithm import get_Shannon_codes
from ShannonFano_algorithm import get_ShannonFano_codes
from arithmetic_coding_algorithm import get_arithmetic_coding_code, decode_arithmetic_coding_code
from LZ_algorithm import get_LZ78_code, decode_LZ78_code

from useful_functions_to_work_with_project import *


def test_small_text():
    start_string = "It goes without saying, books are our teachers and friends. " \
                   "They teach us to be kind, clever, polite, hardworking, friendly. " \
                   "Books help us to learn more about nature, the world around us " \
                   "and many other interesting things.<EOF>"
    my_string = is_string_right(start_string)
    alphabet = make_alphabet(my_string, 1)
    double_alphabet = make_alphabet(my_string, 2)

    all_symbols, count = get_dict_of_symbols(my_string, alphabet)
    all_symbols_probability = dict()

    all_double_symbols, double_count = get_dict_of_symbols(my_string, double_alphabet)
    all_double_symbols_probability = dict()

    for x in all_symbols.keys():
        all_symbols_probability[x] = all_symbols[x] / count
    for x in all_double_symbols.keys():
        all_double_symbols_probability[x] = all_double_symbols[x] / double_count

    Shannon_codes = get_Shannon_codes(list(all_symbols_probability.keys()), list(all_symbols_probability.values()))
    ShannonFano_codes = get_ShannonFano_codes(list(all_symbols_probability.keys()),
                                              list(all_symbols_probability.values()))
    Haffman_codes = get_Haffman_codes(all_symbols)

    Shannon_double_codes = get_Shannon_codes(list(all_double_symbols_probability.keys()),
                                             list(all_double_symbols_probability.values()))
    ShannonFano_double_codes = get_ShannonFano_codes(list(all_double_symbols_probability.keys()),
                                                     list(all_double_symbols_probability.values()))
    Haffman_double_codes = get_Haffman_codes(all_double_symbols)

    # 1) Кодирование Шеноном
    encoded_message = coding(my_string, 1, Shannon_codes)
    decoded_message = bring_string_to_right_form(decoding(encoded_message, Shannon_codes))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"

    # 1.1) Кодирование двойных символов Шеноном
    encoded_message = coding(my_string, 2, Shannon_double_codes)
    decoded_message = decoding(encoded_message, Shannon_double_codes)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя " \
                                         "данный метод кодироания, не совпадают"

    # 2) Кодирование Шеноном-Фано
    encoded_message = coding(my_string, 1, ShannonFano_codes)
    decoded_message = bring_string_to_right_form(decoding(encoded_message, ShannonFano_codes))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"

    # 2.1) Кодирование двойных символов Шеноном-Фано
    encoded_message = coding(my_string, 2, ShannonFano_double_codes)
    decoded_message = decoding(encoded_message, ShannonFano_double_codes)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя " \
                                         "данный метод кодироания, не совпадают"

    # 3) Кодирование Хаффманом
    encoded_message = coding(my_string, 1, Haffman_codes)
    decoded_message = bring_string_to_right_form(decoding(encoded_message, Haffman_codes))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"

    # 3.1) Кодирование двойных символов Хаффманом
    encoded_message = coding(my_string, 2, Haffman_double_codes)
    decoded_message = decoding(encoded_message, Haffman_double_codes)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя " \
                                         "данный метод кодироания, не совпадают"

    # 4) Закодировать и декодировать сообщение, используя адаптивное сжатие по Хаффмену:")
    encoded_message = adaptive_Haffman_code(my_string, alphabet)
    decoded_message = bring_string_to_right_form(decoding_adaptive_Haffman_code(encoded_message, alphabet))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"

    # 5) Закодировать и декодировать, используя адаптивное сжатие по Хаффмену (с символом ESC)")
    encoded_message = adaptive_Haffman_code_with_esc(my_string)
    decoded_message = bring_string_to_right_form(decoding_adaptive_Haffman_code_with_esc(encoded_message))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"

    # 6) Закодировать и декодировать сообщение, используя арифметическое кодирование")
    encoded_message = get_arithmetic_coding_code(my_string, all_symbols_probability)
    decoded_message = bring_string_to_right_form(
        decode_arithmetic_coding_code(encoded_message, all_symbols_probability))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"

    # 7) Закодировать и декодировать сообщение, используя любой
    # из алгоритмов семейства LZ*: LZ77, LZ78, LZW, LZSS2, LZMA2, LZ42"
    encoded_message = get_LZ78_code(my_string)
    decoded_message = bring_string_to_right_form(decode_LZ78_code(encoded_message))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"


def test_big_file():
    start_string = open("Practice_24_03/Task_4_5/test.txt").read() + "<EOF>"
    my_string = is_string_right(start_string)
    alphabet = make_alphabet(my_string, 1)
    double_alphabet = make_alphabet(my_string, 2)

    all_symbols, count = get_dict_of_symbols(my_string, alphabet)
    all_symbols_probability = dict()

    all_double_symbols, double_count = get_dict_of_symbols(my_string, double_alphabet)
    all_double_symbols_probability = dict()

    for x in all_symbols.keys():
        all_symbols_probability[x] = all_symbols[x] / count
    for x in all_double_symbols.keys():
        all_double_symbols_probability[x] = all_double_symbols[x] / double_count

    Shannon_codes = get_Shannon_codes(list(all_symbols_probability.keys()), list(all_symbols_probability.values()))
    ShannonFano_codes = get_ShannonFano_codes(list(all_symbols_probability.keys()),
                                              list(all_symbols_probability.values()))
    Haffman_codes = get_Haffman_codes(all_symbols)

    Shannon_double_codes = get_Shannon_codes(list(all_double_symbols_probability.keys()),
                                             list(all_double_symbols_probability.values()))
    ShannonFano_double_codes = get_ShannonFano_codes(list(all_double_symbols_probability.keys()),
                                                     list(all_double_symbols_probability.values()))
    Haffman_double_codes = get_Haffman_codes(all_double_symbols)

    # 1) Кодирование Шеноном
    encoded_message = coding(my_string, 1, Shannon_codes)
    decoded_message = bring_string_to_right_form(decoding(encoded_message, Shannon_codes))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"

    # 1.1) Кодирование двойных символов Шеноном
    encoded_message = coding(my_string, 2, Shannon_double_codes)
    decoded_message = decoding(encoded_message, Shannon_double_codes)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя " \
                                         "данный метод кодироания, не совпадают"

    # 2) Кодирование Шеноном-Фано
    encoded_message = coding(my_string, 1, ShannonFano_codes)
    decoded_message = bring_string_to_right_form(decoding(encoded_message, ShannonFano_codes))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"

    # 2.1) Кодирование двойных символов Шеноном-Фано
    encoded_message = coding(my_string, 2, ShannonFano_double_codes)
    decoded_message = decoding(encoded_message, ShannonFano_double_codes)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя " \
                                         "данный метод кодироания, не совпадают"

    # 3) Кодирование Хаффманом
    encoded_message = coding(my_string, 1, Haffman_codes)
    decoded_message = bring_string_to_right_form(decoding(encoded_message, Haffman_codes))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"

    # 3.1) Кодирование двойных символов Хаффманом
    encoded_message = coding(my_string, 2, Haffman_double_codes)
    decoded_message = decoding(encoded_message, Haffman_double_codes)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя " \
                                         "данный метод кодироания, не совпадают"

    # 4) Закодировать и декодировать сообщение, используя адаптивное сжатие по Хаффмену:")
    encoded_message = adaptive_Haffman_code(my_string, alphabet)
    decoded_message = bring_string_to_right_form(decoding_adaptive_Haffman_code(encoded_message, alphabet))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"

    # 5) Закодировать и декодировать, используя адаптивное сжатие по Хаффмену (с символом ESC)")
    encoded_message = adaptive_Haffman_code_with_esc(my_string)
    decoded_message = bring_string_to_right_form(decoding_adaptive_Haffman_code_with_esc(encoded_message))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"

    # 6) Закодировать и декодировать сообщение, используя арифметическое кодирование")
    encoded_message = get_arithmetic_coding_code(my_string, all_symbols_probability)
    decoded_message = bring_string_to_right_form(
        decode_arithmetic_coding_code(encoded_message, all_symbols_probability))
    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"

    # 7) Закодировать и декодировать сообщение, используя любой
    # из алгоритмов семейства LZ*: LZ77, LZ78, LZW, LZSS2, LZMA2, LZ42"
    encoded_message = get_LZ78_code(my_string)
    decoded_message = bring_string_to_right_form(decode_LZ78_code(encoded_message))

    assert start_string == decoded_message, "Строка и раскодированая строка, используя " \
                                            "данный метод кодироания, не совпадают"


def test_is_right_coding():
    my_string = "abcbbbbbacabbacddacdbbaccbbadadaddd abcccccbacabbacbbaddbdaccbbddadadcc " \
                "bcabbcdabacbbacbbddcbbaccbbdbdadaac<EOF>"
    my_string = is_string_right(my_string)
    alphabet = make_alphabet(my_string, 1)
    double_alphabet = make_alphabet(my_string, 2)

    all_symbols, count = get_dict_of_symbols(my_string, alphabet)
    all_symbols_probability = dict()

    all_double_symbols, double_count = get_dict_of_symbols(my_string, double_alphabet)
    all_double_symbols_probability = dict()

    for x in all_symbols.keys():
        all_symbols_probability[x] = all_symbols[x] / count
    for x in all_double_symbols.keys():
        all_double_symbols_probability[x] = all_double_symbols[x] / double_count

    Shannon_codes = get_Shannon_codes(list(all_symbols_probability.keys()), list(all_symbols_probability.values()))
    ShannonFano_codes = get_ShannonFano_codes(list(all_symbols_probability.keys()),
                                              list(all_symbols_probability.values()))
    Haffman_codes = get_Haffman_codes(all_symbols)

    Shannon_double_codes = get_Shannon_codes(list(all_double_symbols_probability.keys()),
                                             list(all_double_symbols_probability.values()))
    ShannonFano_double_codes = get_ShannonFano_codes(list(all_double_symbols_probability.keys()),
                                                     list(all_double_symbols_probability.values()))
    Haffman_double_codes = get_Haffman_codes(all_double_symbols)

    # 1) Кодирование Шеноном
    encoded_message = coding(my_string, 1, Shannon_codes)
    assert encoded_message == "010001000000000000010100010000001010011011001010011000000101001000000010110010110" \
                              "010110110110111110010001001001001001000001010001000000101000000010110110001100101" \
                              "001000000110110010110010110100100111110001000100000100110010000101000000010100000" \
                              "011011010000000101001000000110001100101100100101001111110", \
        "Закодированная строка и закодированаая с помощью стороннего кодера строка," \
        " используя данный метод кодироания, не совпадают"

    # 1.1) Кодирование Шеноном по 2 символа
    encoded_message = coding(my_string, 2, Shannon_double_codes)
    assert encoded_message == "01010001010101001110101001010111010010111101001110000010010001001100011101" \
                              "00101110011100100001110101001000000101100010000111000100001000100110101110" \
                              "11110110101110110100001000000100001000110101010011100010001000111100111101111110", \
        "Закодированная строка и закодированаая с помощью стороннего кодера строка," \
        " используя данный метод кодироания, не совпадают"

    # 2) Кодирование Хаффманом по 2 символа
    encoded_message = coding(my_string, 2, Haffman_double_codes)
    assert encoded_message == "0011101110111000000101110011010100111110000110011010010100101000000110101101011100" \
                              "0000101111001110010111100011011110100101010010001110111001101110100111100111101111" \
                              "10100111000011011111111100010101101101100", \
        "Закодированная строка и закодированаая с помощью стороннего кодера строка," \
        " используя данный метод кодироания, не совпадают"

    # 3) Кодирование Шеноном-Фано по 2 символа
    encoded_message = coding(my_string, 2, ShannonFano_double_codes)
    assert encoded_message == "01100010111011100011001110000101100010111000000010100101100111101011110101101" \
                              "00001000110010000011100110101000001010010010110111111001110001111100010001000" \
                              "001000101011011101110000010101010111101111110111111", \
        "Закодированная строка и закодированаая с помощью стороннего кодера строка," \
        " используя данный метод кодироания, не совпадают"

    # 4) Закодировать и декодировать сообщение, используя адаптивное сжатие по Хаффмену:")
    encoded_message = adaptive_Haffman_code(my_string, alphabet)
    assert encoded_message == "101001010111000011110100010111110011011011000111111011001111110110110001100110110" \
                              "000011011011011000000110001011111100111111000100111001100001111100100101011010110" \
                              "000100111000011110001100110100111110011111001001001111000110111100111011000110001" \
                              "000000", \
        "Закодированная строка и закодированаая с помощью стороннего кодера строка," \
        " используя данный метод кодироания, не совпадают"

    # 5) Закодировать и декодировать, используя адаптивное сжатие по Хаффмену (с символом ESC)")
    encoded_message = adaptive_Haffman_code_with_esc(my_string)
    assert encoded_message == "101100001001100010010110001101001101101100001000011101011001001101010110110111010" \
                              "110111110101101101101100110110000010010000010110110110000001100010111111001111110" \
                              "001001110011000011111001001010110101100001001011000011110001100110100111110011111" \
                              "0010010011110001101111001110110001100010000000", \
        "Закодированная строка и закодированаая с помощью стороннего кодера строка," \
        " используя данный метод кодироания, не совпадают"
