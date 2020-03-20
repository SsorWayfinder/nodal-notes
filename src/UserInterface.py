from src.Note import Note
import yaml


def main():
    print("Welcome to Nodal Notes!")
    print("Current commands are:")
    quit_commanded = False
    while not quit_commanded:
        commands = input(':')
        commands = commands.split(' ')
        if len(commands) < 1:
            print("Please input a command.")
            continue
        if commands[0] not in command_functions.keys():
            print(commands[0] + " is not a valid command.")
            continue
        command_functions[commands[0]](commands[1:])


def new(in_args):
    name = in_args[0]
    note = Note(name)
    open_notes[name] = note


def add_content(in_args):
    name = in_args[0]
    if name not in open_notes.keys():
        print("Note " + name + " is not open!")
        return
    content_to_add = input("Add:\n")
    note = open_notes[name]
    note.content += content_to_add


def connect_notes(in_args):
    from_name = in_args[0]
    to_name = in_args[1]
    connection_name = in_args[2]
    if from_name not in open_notes.keys():
        print("Note " + from_name + " is not open!")

    if to_name not in open_notes.keys():
        print("Note " + to_name + " is not open!")

    from_node = open_notes[from_name]
    from_node.add_node(open_notes[to_name], connection_name)


def save(in_args):
    name = in_args[0]
    note_name = in_args[1]
    if note_name not in open_notes.keys():
        print("Note " + note_name + " is not open!")
    file = open(name, "w")
    file.write(open_notes[note_name].serialize())
    file.close()


def load(in_args):
    name = in_args[0]
    note_name = in_args[1]
    file = open(name, 'r')
    file_content = file.read()
    if len(file_content) < 1:
        print("File was empty! Not loaded.")
        return
    open_notes[note_name] = yaml.load(file_content)


command_functions = {"new": new, "add": add_content, "connect": connect_notes, "save": save, "load": load}
open_notes = dict()

if __name__ == "__main__":
    main()
