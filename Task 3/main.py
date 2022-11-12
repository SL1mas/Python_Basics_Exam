# Sukurkite funkciją "addDigits", kuri priims sveiką skaičių nuo 10 iki 999 ir grąžins jo skaitmenų sumą.

# Pvz.
# Jeigu duota 34, funckiją turėtų grąžinti 7.
# Jeigu duota 999, funckija turėtų grąžinti 27.


try:
    number = int(input("Įveskite skaičių nuo 10 iki 999 "))

    def add_digits(number):
        sum_of_digits = 0
        if len(str(number)) > 1 and len(str(number)) < 4:
            for digit in range(0, len(str(number))):
                digit = str(number)[digit]
                sum_of_digits += int(digit)
            return print("Įvesto skaičiaus skaitmenų suma:", sum_of_digits)
        else:
            print("Įvestas skaičius nepatenka į intervalą nuo 10 iki 999!!!")
    sum_of_digits = add_digits(number)
except:
    print("Programa priima tik sveikus skaičius nuo 10 iki 999!!!")
