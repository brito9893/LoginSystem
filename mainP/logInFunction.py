from model.occurrence import Occurrence
from registry.fullHistory import FullHistory
from registry.userRegistry import UserRegistry

ur = UserRegistry()
fh = FullHistory()


def logIn(user, pa):
    for u in ur.userList:
        if u.username == user and u.password == hash(pa):
            print("SUCCESS\n\n")
            occ: Occurrence = Occurrence(u, "Logged in")
            createNewLogAutoTime(occ)
            return True
        else:
            print("FAILURE\n\n")
            return False
