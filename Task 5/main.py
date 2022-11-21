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


result = get_sum_of_multiplied_arrays(array1, array2)
print(f"The sums of {len(array1)} multiplied arrays is: {result}")
