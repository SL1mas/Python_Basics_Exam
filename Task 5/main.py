# Sukurkite funkciją, kuri sudaugintų (NxN) matricas (two dimensional arrays) ir gražintų rezultatą.

# 🤷‍♂️ Čia nėra jokių konkrečių nurodymų 🤷‍♂️ Pagalvokite, ką darytumėte, jei jums būtų duota tokia užduotis darbe.

import numpy as multiplication

array1 = multiplication.array([[5, 2], [3, 1]])
array2 = multiplication.array([[4, 6], [5, 2]])
#    5*4+2*5=30; 5*6+2*2=34; 3*4+1*5=17; 3*6+1*2=20


def get_sum_of_multiplied_arrays(array1, array2):
    print("1st array : ", array1)
    print("2nd array : ", array2)
    return multiplication.dot(array1, array2)

# def get_sum_of_multiplied_arrays(array1, array2):
#     transformed_array_full = []
#     for times in range(0, len(array2)):
#         transformed_array = []
#         for rows2 in array2:
#             transformed_array.append(rows2[times])
#         transformed_array_full.append(transformed_array)
#     print(transformed_array_full)
#     times = 0
#     sum = 0
#     for rows in array1:
#         print(len(array1)-1)
#         print(rows)
#         print(f"**********{times}**********")
#         first_row_to_multiply = array1[times]
#         second_row_to_multiply = transformed_array_full[times]
#         print(f"The sum(-s) of {times+1} array(-s):  {first_row_to_multiply}")
#         print(f"Multiplied by array No.{times+2}: {second_row_to_multiply}")
#         for columns in range(0, len(transformed_array_full)):
#             print("pirmas", first_row_to_multiply[columns])
#             print("antras", second_row_to_multiply[columns])
#             multiplication = first_row_to_multiply[columns] * \
#                 second_row_to_multiply[columns]
#             print("sudauginus", multiplication)
#             sum += multiplication
#         print("suma", sum)

#         times += 1


result = get_sum_of_multiplied_arrays(array1, array2)
print(f"The sums of {len(array1)} multiplied arrays is: {result}")
