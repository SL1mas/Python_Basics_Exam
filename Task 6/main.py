# Sukurkite terminalo programą, kuri bankui leis apdoroti gaunamas užklausas. Bankas gali gauti trijų tipų užklausas:

# - transfer i j sum: prašymas pervesti pinigų sumą iš i-osios sąskaitos į j-ąją;
# - deposit i sum: prašymas įnešti pinigų sumą į i-ąją sąskaitą;
# - withdraw i sum: prašymas išsiimti pinigų sumą iš i-osios sąskaitos.

# Jūsų programa taip pat turėtų galėti apdoroti netinkamas užklausas. Yra dviejų tipų negaliojančios užklausos:
# - neteisingas sąskaitos numeris prašymuose;
# - didesnės pinigų sumos, nei yra šiuo metu, išėmimas/pervedimas.

# Po kiekvienos operacijos išveskite ar ji pavyko, ar ne ir parodykite sąskaitų balansus ekrane.

######################

# Pvz. Kai duoti pradiniai sąskaitų balansai yra:
# ACCOUNTS = [10, 100, 20, 50, 30]

# Įvestos užklausos į terminalą:
# - "withdraw 2 10"
# - "transfer 5 1 20"
# - "deposit 5 20"
# - "transfer 3 4 15"

# Atitinkamai išvedami rezultatai, po kiekvienos užklausos:
# - Operation was successful; New account balances: [10, 90, 20, 50, 30]
# - Operation was successful; New account balances: [30, 90, 20, 50, 10]
# - Operation was successful; New account balances: [30, 90, 20, 50, 30]
# - Operation was successful; New account balances: [10, 90, 20, 50, 30]
# - Operation was successful; New account balances: [30, 90, 5, 65, 30]

######################

# Pvz. Kai duoti pradiniai sąskaitų balansai yra:
# ACCOUNTS = [20, 1000, 500, 40, 90]

# Įvestos užklausos į terminalą:
# - "deposit 3 400"
# - "transfer 1 10 10"
# - "withdraw 4 50"

# Atitinkamai išvedami rezultatai, po kiekvienos užklausos:
# - Operation was successful; New account balances: [20, 1000, 900, 40, 90]
# - Operation is invalid, such account does not exist; New account balances: [20, 1000, 900, 40, 90]
# - Operation is invalid, not enough balance; New account balances: [20, 1000, 900, 40, 90]

# !!! Pastaba: Papildomas taškas, jeigu panaudosite klases. !!!

ACCOUNTS = [10, 100, 20, 50, 30]
# - "withdraw 2 10"
# - "deposit 5 20"
# - "transfer 5 1 20"
print(ACCOUNTS[0])


def withdraw(account):
    pass


def type_in_command_line():
    command_line = list(
        map(str, input("Please type in prefared command or 'help': ").split()))
    if command_line[0] == 'help':
        print("-=*HELP OPTIONS*=- \n Type in: \n • 'c' for command list \n • 'e' for command examples")
        type_in_command_line()
    if command_line[0] == "c":
        print("-=*Command list:\n Type in: \n • 'w' for withdraw \n • 'd' for deposit \
            \n • 't' for transfer \n • 'a' for current accounts balances")
        type_in_command_line()
    if command_line[0] == "e":
        print("-=*Command examples: \n 'w 2 10' from account No.2 withdraw 10 \
            \n 'd 3 20' deposit 20 to account No.3 \
            \n 't 5 2 40' from account No.5 transfer 40 to account No.2 \
            \n -=*Structure of command line: \n • letter for command\n • first number - choosing account \
            \n • second number - amount or choosing second account (transfer command case) \
            \n • third number - amount (transfer command case)")
        type_in_command_line()
    print("Command ", command_line)


command_line = type_in_command_line()
# command_line = list(map(str, input(
#     "Please type in prefared command or 'help': ").split()))
# print(len(command_line))
