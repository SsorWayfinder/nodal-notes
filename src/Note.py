import time
import yaml
import copy


class Note:

    default_nodes_list = "connected"

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

    def add_node(self, note, list_name: str = default_nodes_list):
        if list_name not in self.__Nodes.keys():
            self.__Nodes[list_name] = list()
        self.__Nodes[list_name].append(note)
        self._update_time_stamps()

    def get_nodes(self, list_name: str = default_nodes_list):  # TODO add a more general function that takes a name
        return self.__Nodes[list_name]

    def _update_time_stamps(self):  # , previous):
        previous_lines = list()
        if len(self.TimeStamps) > 0:
            previous_lines = self.TimeStamps[max(self.TimeStamps.keys())].split('\t')

        previous_length = len(previous_lines)
        for i in range(previous_length):
            previous_lines[i] = previous_lines[i][3:]

        current_copy = copy.deepcopy(self)
        current_copy.TimeStamps.clear()
        current_lines = current_copy.serialize().split('\n')
        current_length = len(current_lines)
        result = list()
        for i in range(current_length):
            if i >= len(previous_lines):
                result.append(str(i) + "+ " + current_lines[i])
                continue
            if previous_lines[i] == current_lines[i]:
                continue
            result.append(str(i) + "c " + previous_lines[i] + "-->>" + current_lines[i])
        if current_length < previous_length:
            for i in range(previous_length - current_length):
                index = current_length + i
                result.append(str(index) + "- " + previous_lines[index])

        current_time = time.time()
        if current_time in self.TimeStamps.keys():
            current_time += .0000001
        self.TimeStamps[current_time] = '\t'.join(result)

    def serialize(self):
        return yaml.dump(self)
