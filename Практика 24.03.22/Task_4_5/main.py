from Haffman_algorithm import get_Haffman_codes, adaptive_Haffman_code, decoding_adaptive_Haffman_code, \
    adaptive_Haffman_code_with_esc, decoding_adaptive_Haffman_code_with_esc
from Shannon_algorithm import get_Shannon_codes
from ShannonFano_algorithm import get_ShannonFano_codes
from arithmetic_coding_algorithm import get_arithmetic_coding_code, decode_arithmetic_coding_code
from LZ_algorithm import get_LZ78_code, decode_LZ78_code

from useful_functions_to_work_with_project import *

def print_all_results_of_test(my_string):
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
    ShannonFano_codes = get_ShannonFano_codes(list(all_symbols_probability.keys()), list(all_symbols_probability.values()))
    Haffman_codes = get_Haffman_codes(all_symbols)

    Shannon_double_codes = get_Shannon_codes(list(all_double_symbols_probability.keys()),
                                             list(all_double_symbols_probability.values()))
    ShannonFano_double_codes = get_ShannonFano_codes(list(all_double_symbols_probability.keys()),
                                                     list(all_double_symbols_probability.values()))
    Haffman_double_codes = get_Haffman_codes(all_double_symbols)

    print(f"1) Определить энтропию --> {get_total_entropy_of_codes(list(all_symbols_probability.values()))}\n")

    print(f"2) Построить коды Шеннона, Шеннона–Фано и Хаффмана для отдельных символов:")
    print(f"Код Шенона --> {Shannon_codes}")
    print(f"Код Шенона-Фано --> {ShannonFano_codes}")
    print(f"Код Хаффмана --> {Haffman_codes}\n")

    print(f"3) Построить коды Шеннона, Шеннона–Фано и Хаффмана для двухбуквенных блоков символов:")
    print(f"Код Шенона --> {Shannon_double_codes}")
    print(f"Код Шенона-Фано --> {ShannonFano_double_codes}")
    print(f"Код Хаффмана --> {Haffman_double_codes}\n")

    print(f"4) Закодировать сообщение(По Шеннону например):")
    print(coding(my_string, Shannon_codes) + "\n")

    print(f"5) Определить среднюю длину и избыточность для всех кодов:")
    print(
        f"По Шеннону --> "
        f"средняя длина: {get_average_lenght(list(all_symbols_probability.values()), list(Shannon_codes.values()))}, "
        f"избыточность: {get_message_redundancy(list(all_symbols_probability.values()), list(Shannon_codes.values()))}")
    print(
        f"По Шеннону-Фано --> "
        f"средняя длина: {get_average_lenght(list(all_symbols_probability.values()), list(ShannonFano_codes.values()))}, "
        f"избыточность: {get_message_redundancy(list(all_symbols_probability.values()), list(ShannonFano_codes.values()))}")
    print(
        f"По Хаффману --> "
        f"средняя длина: {get_average_lenght(list(all_symbols_probability.values()), list(Haffman_codes.values()))}, "
        f"избыточность: {get_message_redundancy(list(all_symbols_probability.values()), list(Haffman_codes.values()))}\n")

    print("6) Закодировать и декодировать сообщение, используя адаптивное сжатие по Хаффмену:")
    encoded_message = adaptive_Haffman_code(my_string, alphabet)
    # print(f"Закодированное сообщение --> {encoded_message}")
    decoded_message = decoding_adaptive_Haffman_code(encoded_message, alphabet)
    # print(f"Раскодированное сообщение --> {decoded_message}")
    print(
        f"Сравним нашу строку и полученную после декодирования"
        f" --> {my_string == decoded_message}\n")

    print(f"7) Закодировать и декодировать, используя адаптивное сжатие по Хаффмену (с символом ESC)")
    encoded_message = adaptive_Haffman_code_with_esc(my_string)
    # print(f"Закодированное сообщение --> {encoded_message}")
    decoded_message = decoding_adaptive_Haffman_code_with_esc(encoded_message)
    # print(f"Раскодированное сообщение --> {decoded_message}")
    print(
        f"Сравним нашу строку и полученную после декодирования --> "
        f"{my_string == decoded_message}\n")
    print(f"8) Закодировать и декодировать сообщение, используя арифметическое кодирование")
    encoded_message = get_arithmetic_coding_code(my_string, all_symbols_probability)
    # print(f"Закодированное сообщение --> {encoded_message}")
    decoded_message = decode_arithmetic_coding_code(encoded_message, all_symbols_probability)
    # print(f"Раскодированное сообщение --> {decoded_message}")
    print(
        f"Сравним нашу строку и полученную после декодирования --> "
        f"{my_string == decoded_message}\n")

    print(f"9) Закодировать и декодировать сообщение, используя любой из "
          f"алгоритмов семейства LZ*: LZ77, LZ78, LZW, LZSS2, LZMA2, LZ42 , . . .")
    encoded_message = get_LZ78_code(my_string)
    # print(f"Закодированное сообщение --> {encoded_message}")
    decoded_message = decode_LZ78_code(encoded_message)
    # print(f"Раскодированное сообщение --> {decoded_message}")
    print(
        f"Сравним нашу строку и полученную после декодирования --> "
        f"{my_string == decoded_message}\n")

my_string = "abcbbbbbacabbacddacdbbaccbbadadaddd abcccccbacabbacbbaddbdaccbbddadadcc  bcabbcdabacbbacbbddcbbaccbbdbdadaac<EOF>"
print_all_results_of_test(my_string)
print("----------------------------------------------------------------------")

my_string = "It goes without saying, books are our teachers and friends. " \
            "They teach us to be kind, clever, polite, hardworking, friendly. " \
            "Books help us to learn more about nature, the world around us and many other interesting things.<EOF>"
print_all_results_of_test(my_string)

print("----------------------------------------------------------------------")

my_string = open("test.txt").read() + "<EOF>"
print_all_results_of_test(my_string)