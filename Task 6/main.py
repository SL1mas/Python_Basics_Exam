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

# class Terminal:
#     def __init__(self, account, sum):
#         self.account = account
#         self.suma = sum

#     def withdraw_command(self, account, sum):
#         withdraw = ACCOUNTS[command_line[1]]
#     def deposit_command(self, account, sum):
#     def transfer_command(self, account, sum):

# class Terminal_transfer(Terminal):
#     def __init__(self, account, account_to, sum):
#         super().__init__(self, account, sum)
#         self.account_to = account_to

# terminal = Terminal()


def withdraw(command_line):
    ats = ACCOUNTS[int(command_line[1])-1]-int(command_line[2])
    ACCOUNTS[int(command_line[1])-1] = ats
    return print("Pakoreguoti duomenys", ACCOUNTS)


def type_in_command_line():
    command_line = list(
        map(str, input("Please type in prefared command or 'help': ").split()))
    return command_line


command_line = type_in_command_line()
print("Pradiniai duomenys", ACCOUNTS)
print(command_line[0], command_line[1], command_line[2])
# print("Iš sąskaita", ACCOUNTS[command_line[1]])
# print(ACCOUNTS[int(command_line[1])])
# print(command_line[1])
# print("Suma, kurią atims", command_line[2])

ats = withdraw(command_line)
# print("Pakoreguoti duomenys", ACCOUNTS)

# def type_in_command_line():
#     command_line = list(
#         map(str, input("Please type in prefared command or 'help': ").split()))
#     if command_line[0] == 'help':
#         print("-=*HELP OPTIONS*=- \n Type in: \n • 'c' for command list \n • 'e' for command examples")
#         type_in_command_line()
#     if command_line[0] == "c":
#         print("-=*Command list:\n Type in: \n • 'w' for withdraw \n • 'd' for deposit \
#             \n • 't' for transfer \n • 'a' for current accounts balances")
#         type_in_command_line()
#     if command_line[0] == "e":
#         print("-=*Command examples: \n 'w 2 10' from account No.2 withdraw 10 \
#             \n 'd 3 20' deposit 20 to account No.3 \
#             \n 't 5 2 40' from account No.5 transfer 40 to account No.2 \
#             \n -=*Structure of command line: \n • letter for command\n • first number - choosing account \
#             \n • second number - amount or choosing second account (transfer command case) \
#             \n • third number - amount (transfer command case)")
#         type_in_command_line()
#     print("Command ", command_line)


# command_line = type_in_command_line()
