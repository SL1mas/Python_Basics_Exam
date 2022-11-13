# Sukurkite funkciją, kuri sudaugintų (NxN) matricas (two dimensional arrays) ir gražintų rezultatą.

# 🤷‍♂️ Čia nėra jokių konkrečių nurodymų 🤷‍♂️ Pagalvokite, ką darytumėte, jei jums būtų duota tokia užduotis darbe.
array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [
    11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]


def get_sum_of_multiplied_arrays(array):
    times = 0
    for rows in range(0, len(array)-1):
        print(f"**********{times+1}**********")
        if rows == 0:
            first_row_to_multiply = array[0]
        else:
            first_row_to_multiply = temporary_array
        second_row_to_multiply = array[times+1]
        print(f"The sum(-s) of {times+1} array(-s):  {first_row_to_multiply}")
        print(f"Multiplied by array No.{times+2}: {second_row_to_multiply}")
        times += 1
        temporary_array = []
        for columns in range(0, len(array[times])):
            multiplication = first_row_to_multiply[columns] * \
                second_row_to_multiply[columns]
            temporary_array.append(multiplication)
        print(f"Is: {temporary_array}")
    return temporary_array


temporary_array = get_sum_of_multiplied_arrays(array)
print(f"The sums of {len(array)} multiplied arrays is: {temporary_array}")
