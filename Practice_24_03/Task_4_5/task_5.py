from Haffman_algorithm import get_Haffman_codes, adaptive_Haffman_code, decoding_adaptive_Haffman_code, \
    adaptive_Haffman_code_with_esc, decoding_adaptive_Haffman_code_with_esc
from Shannon_algorithm import get_Shannon_codes
from ShannonFano_algorithm import get_ShannonFano_codes
from arithmetic_coding_algorithm import get_arithmetic_coding_code, decode_arithmetic_coding_code
from LZ_algorithm import get_LZ78_code, decode_LZ78_code

from useful_functions_to_work_with_project import *


def test_small_text():
    my_string = "It goes without saying, books are our teachers and friends. " \
                "They teach us to be kind, clever, polite, hardworking, friendly. " \
                "Books help us to learn more about nature, the world around us and many other interesting things.<EOF>"
    alphabet = make_alphabet(my_string, 1)
    double_alphabet = make_alphabet(my_string, 2)

    all_symbols, count = get_dict_of_symbols(my_string, alphabet)
    all_symbols_probability = dict()

    all_double_symbols, double_count = get_dict_of_symbols(my_string, double_alphabet)
    all_double_symbols_probability = dict()

    for x in all_symbols.keys():
        all_symbols_probability[x] = all_symbols[x] / count
    for x in all_double_symbols.keys():
        all_double_symbols_probability[x] = all_double_symbols[x] / count

    Shannon_codes = get_Shannon_codes(list(all_symbols_probability.keys()), list(all_symbols_probability.values()))
    ShannonFano_codes = get_ShannonFano_codes(list(all_symbols_probability.keys()),
                                              list(all_symbols_probability.values()))
    Haffman_codes = get_Haffman_codes(all_symbols)

    # Shannon_double_codes = get_Shannon_codes(list(all_double_symbols_probability.keys()), list(all_double_symbols_probability.values()))
    # ShannonFano_double_codes = get_ShannonFano_codes(list(all_double_symbols_probability.keys()), list(all_double_symbols_probability.values()))
    # Haffman_double_codes = get_Haffman_codes(all_double_symbols)

    # 1) Кодирование Шеноном
    encoded_message = coding(my_string, 1, Shannon_codes)
    decoded_message = decoding(encoded_message, Shannon_codes)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 1.1) Кодирование двойных символов Шеноном
    # encoded_message = coding(my_string, 2, Shannon_double_codes)
    # decoded_message = decoding(encoded_message, Shannon_double_codes)
    # assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 2) Кодирование Шеноном-Фано
    encoded_message = coding(my_string, 1, ShannonFano_codes)
    decoded_message = decoding(encoded_message, ShannonFano_codes)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 2.1) Кодирование двойных символов Шеноном-Фано
    # encoded_message = coding(my_string, 2, ShannonFano_double_codes)
    # decoded_message = decoding(encoded_message, ShannonFano_double_codes)
    # assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 3) Кодирование Хаффманом
    encoded_message = coding(my_string, 1, Haffman_codes)
    decoded_message = decoding(encoded_message, Haffman_codes)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 3.1) Кодирование двойных символов Хаффманом
    # encoded_message = coding(my_string, 2, Haffman_double_codes)
    # decoded_message = decoding(encoded_message, Haffman_double_codes)
    # assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 4) Закодировать и декодировать сообщение, используя адаптивное сжатие по Хаффмену:")
    encoded_message = adaptive_Haffman_code(my_string, alphabet)
    decoded_message = decoding_adaptive_Haffman_code(encoded_message, alphabet)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 5) Закодировать и декодировать, используя адаптивное сжатие по Хаффмену (с символом ESC)")
    encoded_message = adaptive_Haffman_code_with_esc(my_string)
    decoded_message = decoding_adaptive_Haffman_code_with_esc(encoded_message)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 6) Закодировать и декодировать сообщение, используя арифметическое кодирование")
    encoded_message = get_arithmetic_coding_code(my_string, all_symbols_probability)
    decoded_message = decode_arithmetic_coding_code(encoded_message, all_symbols_probability)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 7) Закодировать и декодировать сообщение, используя любой
    # из алгоритмов семейства LZ*: LZ77, LZ78, LZW, LZSS2, LZMA2, LZ42"
    encoded_message = get_LZ78_code(my_string)
    decoded_message = decode_LZ78_code(encoded_message)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"


def test_big_file():
    my_string = open("Practice_24_03/Task_4_5/test.txt").read() + "<EOF>"
    alphabet = make_alphabet(my_string, 1)
    double_alphabet = make_alphabet(my_string, 2)

    all_symbols, count = get_dict_of_symbols(my_string, alphabet)
    all_symbols_probability = dict()

    all_double_symbols, double_count = get_dict_of_symbols(my_string, double_alphabet)
    all_double_symbols_probability = dict()

    for x in all_symbols.keys():
        all_symbols_probability[x] = all_symbols[x] / count
    for x in all_double_symbols.keys():
        all_double_symbols_probability[x] = all_double_symbols[x] / count

    Shannon_codes = get_Shannon_codes(list(all_symbols_probability.keys()), list(all_symbols_probability.values()))
    ShannonFano_codes = get_ShannonFano_codes(list(all_symbols_probability.keys()),
                                              list(all_symbols_probability.values()))
    Haffman_codes = get_Haffman_codes(all_symbols)

    # Shannon_double_codes = get_Shannon_codes(list(all_double_symbols_probability.keys()), list(all_double_symbols_probability.values()))
    # ShannonFano_double_codes = get_ShannonFano_codes(list(all_double_symbols_probability.keys()), list(all_double_symbols_probability.values()))
    # Haffman_double_codes = get_Haffman_codes(all_double_symbols)

    # 1) Кодирование Шеноном
    encoded_message = coding(my_string, 1, Shannon_codes)
    decoded_message = decoding(encoded_message, Shannon_codes)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 1.1) Кодирование двойных символов Шеноном
    # encoded_message = coding(my_string, 2, Shannon_double_codes)
    # decoded_message = decoding(encoded_message, Shannon_double_codes)
    # assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 2) Кодирование Шеноном-Фано
    encoded_message = coding(my_string, 1, ShannonFano_codes)
    decoded_message = decoding(encoded_message, ShannonFano_codes)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 2.1) Кодирование двойных символов Шеноном-Фано
    # encoded_message = coding(my_string, 2, ShannonFano_double_codes)
    # decoded_message = decoding(encoded_message, ShannonFano_double_codes)
    # assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 3) Кодирование Хаффманом
    encoded_message = coding(my_string, 1, Haffman_codes)
    decoded_message = decoding(encoded_message, Haffman_codes)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 3.1) Кодирование двойных символов Хаффманом
    # encoded_message = coding(my_string, 2, Haffman_double_codes)
    # decoded_message = decoding(encoded_message, Haffman_double_codes)
    # assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 4) Закодировать и декодировать сообщение, используя адаптивное сжатие по Хаффмену:")
    encoded_message = adaptive_Haffman_code(my_string, alphabet)
    decoded_message = decoding_adaptive_Haffman_code(encoded_message, alphabet)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 5) Закодировать и декодировать, используя адаптивное сжатие по Хаффмену (с символом ESC)")
    encoded_message = adaptive_Haffman_code_with_esc(my_string)
    decoded_message = decoding_adaptive_Haffman_code_with_esc(encoded_message)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 6) Закодировать и декодировать сообщение, используя арифметическое кодирование")
    encoded_message = get_arithmetic_coding_code(my_string, all_symbols_probability)
    decoded_message = decode_arithmetic_coding_code(encoded_message, all_symbols_probability)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"

    # 7) Закодировать и декодировать сообщение, используя любой
    # из алгоритмов семейства LZ*: LZ77, LZ78, LZW, LZSS2, LZMA2, LZ42"
    encoded_message = get_LZ78_code(my_string)
    decoded_message = decode_LZ78_code(encoded_message)
    assert my_string == decoded_message, "Строка и раскодированая строка, используя данный метод кодироания, не совпадают"


def test_is_right_coding():
    my_string = "abcbbbbbacabbacddacdbbaccbbadadaddd abcccccbacabbacbbaddbdaccbbddadadcc  bcabbcdabacbbacbbddcbbaccbbdbdadaac<EOF>"
    alphabet = make_alphabet(my_string, 1)

    all_symbols, count = get_dict_of_symbols(my_string, alphabet)
    all_symbols_probability = dict()

    for x in all_symbols.keys():
        all_symbols_probability[x] = all_symbols[x] / count

    Shannon_codes = get_Shannon_codes(list(all_symbols_probability.keys()), list(all_symbols_probability.values()))
    ShannonFano_codes = get_ShannonFano_codes(list(all_symbols_probability.keys()),
                                              list(all_symbols_probability.values()))
    Haffman_codes = get_Haffman_codes(all_symbols)

    # 1) Кодирование Шеноном
    encoded_message = coding(my_string, 1, Shannon_codes)
    assert encoded_message == "010001000000000000010100010000001010011011001010011000000101001000000010110010110" \
                              "010110110110111101010001001001001001000001010001000000101000000010110110001100101" \
                              "001000000110110010110010110100100111101111101001000100000100110010000101000000010" \
                              "100000011011010000000101001000000110001100101100100101001111110", \
        "Закодированная строка и закодированаая с помощью стороннего кодера строка," \
        " используя данный метод кодироания, не совпадают"

    # 2) Кодирование Хаффманом
    encoded_message = coding(my_string, 1, Haffman_codes)
    assert encoded_message == "101101111111111110011011111001001001100100111111001011111100011000110001001001000" \
                              "110110101010101111001101111100111111000100111001100101111100100110001100010101000" \
                              "1000111011011110100110111001111110011111001001011111100101111100111001100011010010000", \
        "Закодированная строка и закодированаая с помощью стороннего кодера строка," \
        " используя данный метод кодироания, не совпадают"

    # 3) Кодирование Шеноном-Фано
    encoded_message = coding(my_string, 1, ShannonFano_codes)
    assert encoded_message == "0100100000000000011001000001101101100110110000001101000000111001110011101" \
                              "1011011100100101010101000011001000001100000011101100011001101000001101100" \
                              "1110011101010111011100010010000101100100011000000110000011011010000001101" \
                              "0000011000110011100101101111", \
        "Закодированная строка и закодированаая с помощью стороннего кодера строка," \
        " используя данный метод кодироания, не совпадают"

    # 4) Закодировать и декодировать сообщение, используя адаптивное сжатие по Хаффмену:")
    encoded_message = adaptive_Haffman_code(my_string, alphabet)
    assert encoded_message == "10001110001110000111101000101111101111011011000111111011001111110110110" \
                              "00110011011000000101101101100000011000101111110011111100010011100110000" \
                              "11111001001010110101100001001100111000011110010100110100111101001111001" \
                              "101001111000010111101111011001010001001000", \
        "Закодированная строка и закодированаая с помощью стороннего кодера строка," \
        " используя данный метод кодироания, не совпадают"

    # 5) Закодировать и декодировать, используя адаптивное сжатие по Хаффмену (с символом ESC)")
    encoded_message = adaptive_Haffman_code_with_esc(my_string)
    assert encoded_message == "101100001001100010010110001101001101101100001000011101011001001101010110" \
                              "1101110101101111101011011011011001101100000100100000101101101100000011000" \
                              "1011111100111111000100111001100001111100100101011010110000100101001110000" \
                              "111100101001101001111010011110011010011110000101111011110110010100010010000", \
        "Закодированная строка и закодированаая с помощью стороннего кодера строка," \
        " используя данный метод кодироания, не совпадают"

