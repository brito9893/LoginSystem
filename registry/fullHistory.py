from model.log import Log


def createNewLog(occurrence, time) -> bool:
    log = Log(occurrence)
    log.changeTime(time)
    FullHistory.history.append(log)
    FullHistory.count += 1
    return log in FullHistory.history


def deleteLog(occurrence, time) -> bool:
    log = Log(occurrence)
    log.changeTime(time)

    FullHistory.history.remove(log)

    return log in FullHistory.history


class FullHistory(object):
    history: list = []
    count = 0

    def __init__(self):
        pass

    @staticmethod
    def createNewLogAutoTime(occurrence) -> bool:
        log = Log(occurrence)
        FullHistory.history.append(log)
        return log in FullHistory.history
