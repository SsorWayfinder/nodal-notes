import unittest
from src import Note


class TestNote(unittest.TestCase):

    def setUp(self):
        self.note = Note.Note("Test")

    def test_init(self):
        # assert
        self.assertEqual("Test", self.note.title)
        self.assertEqual("", self.note.content)
        self.assertEqual(1, len(self.note.TimeStamps))
        first = [v for v in self.note.TimeStamps.values()]
        first = first[0].split('\t')
        self.assertEqual("0+ !!python/object:src.Note.Note", first[0])
        self.assertEqual("1+ TimeStamps: {}", first[1])
        self.assertEqual("2+ _Note__Content: ''", first[2])
        self.assertEqual("3+ _Note__Nodes: {}", first[3])
        self.assertEqual("4+ _Note__Title: Test", first[4])

    def test_add_node(self):
        # arrange
        new_note = Note.Note("New Note")
        self.note.add_node(new_note)
        # act
        result = self.note.get_nodes()
        # assert
        self.assertEqual(1, len(result))
        self.assertEqual(new_note, result[0])

    def test_add_node_circular(self):
        # arrange
        new_note = Note.Note("New Note")
        self.note.add_node(new_note)
        new_note.add_node(self.note)
        # act
        result = new_note.serialize()
        # assert
        self.assertEqual(result[:36], '&id001 !!python/object:src.Note.Note')
        self.assertTrue('*id001' in result)

    def test_serialize(self):
        # arrange
        # act
        result = self.note.serialize()
        # assert
        result = result.split('\n')
        self.assertEqual("!!python/object:src.Note.Note", result[0])
        self.assertEqual("TimeStamps:", result[1])
        # skipped the content of TimeStamps
        self.assertEqual("_Note__Content: ''", result[4])
        self.assertEqual("_Note__Nodes: {}", result[5])
        self.assertEqual("_Note__Title: Test", result[6])

    def test_TimeStampsContent(self):
        # arrange
        self.note.content = "new stuff"
        # act
        result = self.note.TimeStamps
        # assert
        self.assertEqual(2, len(result), result)
        diff = result[max(result.keys())].split('\t')
        self.assertEqual(1, len(diff))
        self.assertEqual("2c _Note__Content: ''-->>_Note__Content: new stuff", diff[0])

    def test_TimeStampsTitle(self):
        # arrange
        self.note.title = 'Something Else'
        # act
        result = self.note.TimeStamps
        # assert
        self.assertEqual(2, len(result))
        diff = result[max(result.keys())].split('\t')
        self.assertEqual(1, len(diff))
        self.assertEqual('4c _Note__Title: Test-->>_Note__Title: Something Else', diff[0])

    def test_TimeStampsNodes(self):
        # arrange
        new_note = Note.Note('New Note')
        self.note.add_node(new_note)
        # act
        result = self.note.TimeStamps
        # assert
        self.assertEqual(2, len(result), result)
        diff = result[max(result.keys())].split('\t')
        self.assertEqual(11, len(diff), diff)
        self.assertEqual('3c _Note__Nodes: {}-->>_Note__Nodes:', diff[0])
        self.assertEqual('4c _Note__Title: Test-->>  connected:', diff[1])
        self.assertEqual('5c -->>  - !!python/object:src.Note.Note', diff[2])
        self.assertEqual('6+     TimeStamps:', diff[3])
        # skipped the line with the actual TimeStamp
        self.assertEqual('8+         \\ _Note__Content: \'\'\\t3+ _Note__Nodes: {}\\t4+ _Note__Title: New Note\\t5+ "',
                         diff[5])
        self.assertEqual("9+     _Note__Content: ''", diff[6])
        self.assertEqual('10+     _Note__Nodes: {}', diff[7])
        self.assertEqual('11+     _Note__Title: New Note', diff[8])
        self.assertEqual('12+ _Note__Title: Test', diff[9])
        self.assertEqual('13+ ', diff[10])



if __name__ == "__main__":
      unittest.main()


