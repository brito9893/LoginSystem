from model.occurrence import Occurrence
from model.user import User
from registry.fullHistory import FullHistory

u: User = User("Vítor Brito", "vitorbrito98@outlook.pt", "Britocom.123", "brito9893")

h = FullHistory()


def checkUser(user, password) -> bool:
    for us in UserRegistry.userList:
        if us.username == user:
            return us.password == hash(password)


def list() -> list:
    return UserRegistry.userList


class UserRegistry(object):
    userList = [u]

    def addUser(self, name, email, user, p):
        us = User(name, email, user, hash(p))
        UserRegistry.userList.append(us)
        createNewLogAutoTime(occurrence=Occurrence(us, "User added to database"))

        if us in self.userList:
            return True
