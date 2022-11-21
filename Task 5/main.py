# Sukurkite funkciją, kuri sudaugintų (NxN) matricas (two dimensional arrays) ir gražintų rezultatą.

# 🤷‍♂️ Čia nėra jokių konkrečių nurodymų 🤷‍♂️ Pagalvokite, ką darytumėte, jei jums būtų duota tokia užduotis darbe.


# ***First method***

import numpy as multiplication

a = multiplication.array(
    [[5, 2, 4, 7, 4], [3, 1, 9, 7, 3], [1, 1, 1, 7, 2], [1, 2, 3, 4, 1], [9, 2, 5, 7, 1]])
b = multiplication.array(
    [[4, 6, 4, 7, 1], [5, 2, 9, 7, 2], [2, 2, 2, 7, 3], [1, 2, 3, 4, 4], [6, 8, 2, 3, 9]])


def get_multiplied_arrays_method1(a, b):
    # print("1st array : ", a)
    # print("2nd array : ", b)
    return multiplication.dot(a, b)


result = get_multiplied_arrays_method1(a, b)
# print(f"Multiplication of 2 arrays: {result}")

# ***Second method***
array1 = [[5, 2, 4, 7, 4], [3, 1, 9, 7, 3], [
    1, 1, 1, 7, 2], [1, 2, 3, 4, 1], [9, 2, 5, 7, 1]]
array2 = [[4, 6, 4, 7, 1], [5, 2, 9, 7, 2], [
    2, 2, 2, 7, 3], [1, 2, 3, 4, 4], [6, 8, 2, 3, 9]]
multiplied = []


def get_multiplied_arrays_method2(array1, array2):
    times = 0

    def get_transformed_array2(array2):
        fully_transformed_array2 = []
        for x in range(0, len(array2)):
            transformed_array = []
            for rows2 in array2:
                transformed_array.append(rows2[x])
            fully_transformed_array2.append(transformed_array)
        return fully_transformed_array2
    fully_transformed_array2 = get_transformed_array2(array2)

    def get_multiplied_array_x():
        def get_multiplied_array_values():
            sum = 0
            for x in range(0, len(array1[times])):
                multiplication = array1[times][x] * \
                    fully_transformed_array2[amount][x]
                sum += multiplication
            multiplied_x.append(sum)
            print("Multiplied value(-s)", multiplied_x)
            return multiplied_x

        print(f"**********{times+1}**********")
        amount = 0
        multiplied_x = []
        while amount <= len(array1[times])-1:
            get_multiplied_array_values()
            amount += 1
        multiplied.append(multiplied_x)

    print("Array 2", array2)
    print("Array 2 rows transformed into columns", fully_transformed_array2)
    print("Array 1", array1)

    for rows in array1:
        get_multiplied_array_x()
        times += 1
    return multiplied


get_multiplied_arrays_method2(array1, array2)
print(f"First method of {len(array1)} arrays multiplication: {result}")
print(f"Second method of {len(array1)} arrays multiplication: {multiplied}")
