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
        first = first[0].split('\\n')
        self.assertEqual("0+ !!python/object:src.Note.Note", first[0])
        self.assertEqual("1+ TimeStamps: {}", first[1])
        self.assertEqual("2+ _Note__Content: ''", first[2])
        self.assertEqual("3+ _Note__Nodes: {}", first[3])
        self.assertEqual("4+ _Note__Title: Test", first[4])

    def test_save(self):
        # arrange
        # act
        self.note.save()
        # assert
        self.assertFalse(True)

    def test_TimeStampsContent(self):
        # arrange
        self.note.content = "new stuff"
        # act
        result = self.note.TimeStamps
        # assert
        self.assertEqual(2, len(result))
        diff = result[max(result.keys())].split('\\n')
        self.assertEqual("9c _Note__Content: ''-->>_Note__Content: new stuff", diff[0])


if __name__ == '__main__':
    unittest.main()
