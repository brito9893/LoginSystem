from datetime import datetime


class Log(object):
    occurrence = ''
    time = -1

    def __init__(self, o):
        self.occurrence = o
        self.time = datetime.now()

    def changeTime(self, time):
        self.time = time
        return
