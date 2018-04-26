import re

from model.occurrence import Occurrence
from model.user import User
from registry.fullHistory import FullHistory

fh: FullHistory = FullHistory()


def register():
    global aux

    aux = input("Insert your name: ")
    while len(aux) == 0:
        print("Invalid name!\n")
        aux = input("Insert your name: ")
        break
    name = aux

    aux = input("Insert your email: ")
    while not verifyEmail(aux):
        print("Invalid email address!\n")
        aux = input("Insert your email: ")
        break
    email = aux

    aux = input("Insert username: ")
    while not verifyUsername(aux):
        print("Username must contain at least:\t5 characters\n")
        aux = input("Insert username: ")
        break
    username = aux

    aux = input("Insert password: ")
    while not verifyPassword(aux):
        print("Password must contain at least:\t8 characters\n")
        aux = input("Insert password: ")
        break
    password = aux

    user: User = User(name, email, password, username)

    occ: Occurrence = Occurrence(user, "Added new user")
    FullHistory.createNewLogAutoTime(occ)

    return name, email


def verifyPassword(p):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[.!@#\$%\^&\*])"
    return re.search(regex, p) and len(p) >= 8


def verifyUsername(u):
    regex = "[A-Za-z0-9]{5,}"
    return re.search(regex, u)


def verifyEmail(email):
    regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.search(regex, email)
