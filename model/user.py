class User(object):
    name = ""
    email = ""
    password = -1
    username = ""

    def __init__(self, name, email, password, username):
        self.name = name
        self.email = email
        self.password = hash(password)
        self.username = username

    def changeName(self, name):
        self.name = name

    def changeEmail(self, email):
        self.email = email

    def changeUsername(self, username):
        self.username = username

    def changePassword(self, password):
        if hash(password) != self.password:
            self.password = hash(password)
        else:
            print("New password must be different from old one!")
