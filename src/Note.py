import time
import yaml
import difflib


class Note:

    def __init__(self, title: str, initial_content: str = ""):
        self.__Title = title
        self.TimeStamps = dict()
        self.__Content = initial_content
        self.__Nodes = dict()
        diff = difflib.unified_diff("", yaml.dump(self).splitlines(1))
        diff = list(diff)
        self.TimeStamps[time.time()] = ''.join(diff) 

    @property
    def Title(self):
        return self.__Title

    @Title.setter
    def Title(self, Title):
        self.__Title = Title
    
    @property
    def Content(self):
        return self.__Content

    @Content.setter
    def Content(self, Content):
        self.__Content = Content

    @property
    def Nodes(self):
        return self.__Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self.__Nodes = Nodes


	
    def save(self, name: str = ""):
        if len(name) == 0:
            name = self.Title
