from mainP.logInFunction import logIn
from mainP.registerFunction import register
from registry import userRegistry


def menu():
    choice = input("Would you like to log in(0), register(1) or exit(-1): ")
    return choice


print("Welcome!\n")
while True:
    option = menu()
    if option == '0':
        username = input("Insert username: ")
        password = input("Insert password: ")

        logIn(username, password)
    elif option == '1':
        print(register())
    elif option == '-1':
        print("Exiting...")
        break
    elif option == '2':
        for u in userRegistry.list():
            print(u.username)

exit(0)
