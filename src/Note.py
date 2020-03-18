import time
import yaml
import difflib


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

    @property
    def content(self):
        return self.__Content

    @content.setter
    def content(self, content):
        self.__Content = content
        self._update_time_stamps()

    @property
    def nodes(self):
        return self.__Nodes

    @nodes.setter
    def nodes(self, nodes):
        self.__Nodes = nodes

    def _update_time_stamps(self):  # , previous):
        # diff = difflib.ndiff(previous.splitlines(), yaml.dump(self).splitlines(1))
        # diff = ''.join(diff)
        previous_lines = list()
        if len(self.TimeStamps) > 0:
            previous_lines = self.TimeStamps[max(self.TimeStamps.keys())].split('\\n')

        previous_length = len(previous_lines)
        for i in range(previous_length):
            previous_lines[i] = previous_lines[i][3:]
        current_lines = yaml.dump(self).split('\n')
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

        self.TimeStamps[time.time()] = '\\n'.join(result)

    def save(self, name: str = ""):
        if len(name) == 0:
            name = self.title
