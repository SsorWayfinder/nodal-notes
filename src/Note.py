import time
import yaml

class Note:

    def __init__(self, title: str, initial_content: str = ""):
        self.Title = title
        self.TimeStamps = dict()
        self.content = initial_content
        self.Nodes = dict()
        self.TimeStamps[time.time()] = yaml.dump(self) 

    def save(self, name: str = ""):
        if len(name) == 0:
            name = self.Title
