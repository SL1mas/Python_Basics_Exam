# Turimas "users" masyvas.

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserMedianAge" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" amžiaus medianą.
# 2. funkcija "getOldestUser" -  kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins vyriausio vartotojo vardą.

users = [
    {"id": '1', "name": 'John Smith', "age": 20},
    {"id": '2', "name": 'Ann Smith', "age": 24},
    {"id": '3', "name": 'Tom Jones', "age": 31},
    {"id": '4', "name": 'Rose Peterson', "age": 17},
    {"id": '5', "name": 'Alex John', "age": 25},
    {"id": '6', "name": 'Ronald Jones', "age": 63},
    {"id": '7', "name": 'Elton Smith', "age": 16},
    {"id": '8', "name": 'Simon Peterson', "age": 30},
    # {"id": '9', "name": 'Daniel Cane', "age": 51},
]


def get_user_median_age(users):
    print(len(users))
    if len(users) % 2 == 0:
        print((users[int(len(users) / 2)-1]["age"] +
              users[int(len(users) / 2)]["age"])/2)
    else:
        print(users[int((len(users) / 2))]["age"])

    # return sorted([user["age"] for user in users])


print("Vartotojų amžiaus mediana", get_user_median_age(users))

# def get_oldest_user(users):
#     pass


# 2.2 task

# def get_users_names(users):
#   return sorted([user["name"] for user in users])

# print(get_users_names(users))
