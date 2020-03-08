import time
import pickle


class Note:

    def __init__(self, title: str, initial_content: str = ""):
        self.Title = title
        self.TimesStamps = dict()
        self.TimesStamps[time.time()] = None
        self.content = initial_content
        self.Nodes = dict()

    def save(self, name: str = ""):
        if len(name) is 0:
            name = self.Title
        file = open(name, 'wb')
        pickle.dump(self, file)
