import unittest
from src import Note


class TestNote(unittest.TestCase):

    def setUp(self):
        self.note = Note.Note("Test")

    def test_init(self):
        # assert
        self.assertEqual("Test", self.note.Title)
        self.assertEqual("", self.note.content)
        self.assertEqual(1, len(self.note.TimesStamps))
        first = [v for v in self.note.TimesStamps.values()]
        self.assertIsNone(first[0])

    def test_save(self):
        # arrange
        # act
        self.note.save()
        # assert
        self.assertFalse(True)




if __name__ == '__main__':
    unittest.main()
