from Task_4_5.useful_functions_to_work_with_project import get_average_lenght
from Task_4_5.ShannonFano_algorithm import get_ShannonFano_codes

ShannonFano_codes = get_ShannonFano_codes(['A', 'B', 'C', 'D'], [0.5, 0.3, 0.1, 0.1])
print(get_average_lenght([0.5, 0.3, 0.1, 0.1], list(ShannonFano_codes.values())))
# Answer B) 1.7
