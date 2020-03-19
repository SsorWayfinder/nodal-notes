import time
import yaml
import copy


class Note:

    def __init__(self, title: str, initial_content: str = ""):
        self.__Title = title
        self.TimeStamps = dict()
        self.__Content = initial_content
        self.__Nodes = dict()
        self._update_time_stamps()

    @property
    def title(self):
        return self.__Title

    @title.setter
    def title(self, title):
        self.__Title = title
        self._update_time_stamps()

    @property
    def content(self):
        return self.__Content

    @content.setter
    def content(self, content):
        self.__Content = content
        self._update_time_stamps()

    def add_node(self, note):
        if 'connected' not in self.__Nodes.keys(): # TODO move to const? 
            self.__Nodes['connected'] = list()
        self.__Nodes['connected'].append( note) # TODO add a more general function that takes a name
        self._update_time_stamps()
    
    def get_nodes(self): # TODO add a more general function that takes a name 
        return self.__Nodes['connected']

    def _update_time_stamps(self):  # , previous):
        # diff = difflib.ndiff(previous.splitlines(), yaml.dump(self).splitlines(1))
        # diff = ''.join(diff)
        previous_lines = list()
        if len(self.TimeStamps) > 0:
            previous_lines = self.TimeStamps[max(self.TimeStamps.keys())].split('\t')

        previous_length = len(previous_lines)
        for i in range(previous_length):
            previous_lines[i] = previous_lines[i][3:]

        current_copy = copy.deepcopy(self)
        current_copy.TimeStamps.clear()
        current_lines = yaml.dump(current_copy).split('\n')
        current_length = len(current_lines)
        result = list()
        for i in range(current_length):
            if i >= len(previous_lines):
                result.append(str(i)+"+ "+current_lines[i])
                continue
            if previous_lines[i] == current_lines[i]:
                continue
            result.append(str(i)+"c "+previous_lines[i]+"-->>"+current_lines[i])
        if current_length < previous_length:
            for i in range(previous_length - current_length):
                index = current_length+i
                result.append(str(index)+"- "+previous_lines[index])

        self.TimeStamps[time.time()] = '\t'.join(result)

    def save(self, name: str = ""):
        if len(name) == 0:
            name = self.title
