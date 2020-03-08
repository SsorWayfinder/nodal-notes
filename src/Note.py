import time


class Note:

    def __init__(self, initial_content: str = ""):
        self.TimesStamps = list()
        self.TimesStamps.append(time.time())
        self.content = initial_content
        self.Nodes = dict()

    def save(self, name):
        pass
