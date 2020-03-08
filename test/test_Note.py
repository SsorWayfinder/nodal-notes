import unittest
from src import Note


class TestNote(unittest.TestCase):

    def setUp(self):
        self.note = Note.Note()

    def test_init(self):
        # assert
        self.assertEquals(1, len(self.note.TimesStamps))
        self.assertEquals("", self.note.content)

    def test_save(self):
        # arrange
        file_name = "note1"
        # act
        self.note.save(file_name)
        # assert
        self.assertFalse(True)




if __name__ == '__main__':
    unittest.main()
