# Sukurkite funkciją, kuri sudaugintų (NxN) matricas (two dimensional arrays) ir gražintų rezultatą.

# 🤷‍♂️ Čia nėra jokių konkrečių nurodymų 🤷‍♂️ Pagalvokite, ką darytumėte, jei jums būtų duota tokia užduotis darbe.
array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [
    11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
new_array = []
times = 0
# 1 [1, 2, 3, 4, 5]
# 2 [6, 7, 8, 9, 10]        1*2=rezultatas 1
# 3 [11, 12, 13, 14, 15]    rezultatas 1*3=rezultatas 2
# 4 [16, 17, 18, 19, 20]    rezultatas 2*4=rezultatas 3
# 5 [21, 22, 23, 24, 25]    rezultatas 3*5=rezultatas 4


def array_multiplication(arra1, array2):
    pass


print(len(array))
print(len(array[0]))
for rows in range(0, len(array)-1):
    # print(rows)
    first_row_to_multiply = array[times]
    second_row_to_multiply = array[times+1]
    print("Row 1", first_row_to_multiply)
    print("Row 2", second_row_to_multiply)
    print("***Tarpas***", times+1)
    times += 1
    for columns in range(0, len(array[times])):
        # first_row_to_multiply = array[0+times]
        # second_row_to_multiply = array[1+times]
        print("Iš Row 1", first_row_to_multiply[columns])
        print("Iš Row 2", second_row_to_multiply[columns])
        print(
            "Daugyba", first_row_to_multiply[columns]*second_row_to_multiply[columns])
    # times += 1
