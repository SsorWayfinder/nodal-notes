import unittest
from src import Note


class TestNote(unittest.TestCase):

    def setUp(self):
        self.note = Note.Note("Test")

    def test_init(self):
        # assert
        self.assertEqual("Test", self.note.Title)
        self.assertEqual("", self.note.content)
        self.assertEqual(1, len(self.note.TimeStamps))
        first = [v for v in self.note.TimeStamps.values()]
        self.assertEqual("!!python/object:src.Note.Note\nNodes: {}\nTimeStamps: {}\nTitle: Test\ncontent: ''\n", first[0])
        self.assertTrue("Title: Test\ncontent: ''\n" in first[0], "Value of the TimeStamp is actually:\n"+ first[0])

    def test_save(self):
        # arrange
        # act
        self.note.save()
        # assert
        self.assertFalse(True)
        
    def test_TimeStamps(self):
      # arrange
      self.note.content = "new stuff"
      # act
      result = self.note.TimeStamps
      # assert
      self.assertEqual(2, len(result))




if __name__ == '__main__':
    unittest.main()
