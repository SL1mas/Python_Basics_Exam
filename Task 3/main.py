# Sukurkite funkciją "addDigits", kuri priims sveiką skaičių nuo 10 iki 999 ir grąžins jo skaitmenų sumą.

# Pvz.
# Jeigu duota 34, funckiją turėtų grąžinti 7.
# Jeigu duota 999, funckija turėtų grąžinti 27.


# def add_digits(number):
sum_of_digits = 0
number = int(input("Įveskite skaičių nuo 10 iki 999 "))
for digit in range(0, len(str(number))):
    digit = str(number)[digit]
    sum_of_digits += int(digit)
print("suma", sum_of_digits)
