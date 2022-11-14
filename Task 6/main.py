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


class Terminal:
    def __init__(self, command, account, sum):
        self.command = command
        self.account = account
        self.sum = sum

    def withdraw_command(self):
        print("Withdraw", self.command, self.account, self.sum)
        withdraw_ats = ACCOUNTS[int(command_line[1])-1]-int(command_line[2])
        ACCOUNTS[int(command_line[1])-1] = withdraw_ats
        print("Nuskaičiavo nuo balanso", ACCOUNTS)

    def deposit_command(self):
        print("Deposit", self.command, self.account, self.sum)
        deposit_ats = ACCOUNTS[int(command_line[1])-1]+int(command_line[2])
        ACCOUNTS[int(command_line[1])-1] = deposit_ats
        print("Pridėjo prie balanso", ACCOUNTS)


class Terminal_transfer:
    def __init__(self, command, account, account_to, sum):
        self.command = command
        self.account = account
        self.account_to = account_to
        self.sum = sum

    def transfer_command(self):
        transfer_from = ACCOUNTS[int(command_line[1])-1]-int(command_line[3])
        ACCOUNTS[int(command_line[1])-1] = transfer_from
        deposit_to = ACCOUNTS[int(command_line[2])-1]+int(command_line[3])
        ACCOUNTS[int(command_line[2])-1] = deposit_to
        print("Pervedė iš į", ACCOUNTS)


def type_in_command_line():
    command_line = list(
        map(str, input("Please type in prefared command or 'help': ").split()))
    return command_line


command_line = type_in_command_line()
print("Pradiniai duomenys", ACCOUNTS)
terminal = Terminal(command_line[0], command_line[1], command_line[2])
terminal_transfer = Terminal_transfer(
    command_line[0], command_line[1], command_line[2], command_line[3])
terminal.withdraw_command()
terminal.deposit_command()
terminal_transfer.transfer_command()

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
