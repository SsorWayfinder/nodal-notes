import unittest
from src import Note


class TestNote(unittest.TestCase):

    def setUp(self):
        self.note = Note.Note("Test")

    def test_init(self):
        # assert
        self.assertEqual("Test", self.note.Title)
        self.assertEqual("", self.note.Content)
        self.assertEqual(1, len(self.note.TimeStamps))
        first = [v for v in self.note.TimeStamps.values()]
        self.assertEqual("--- \n+++ \n@@ -0,0 +1,5 @@\n+!!python/object:src.Note.Note\n+TimeStamps: {}\n+_Note__Content: ''\n+_Note__Nodes: {}\n+_Note__Title: Test\n", first[0], 'first diff was:\n'+first[0])

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
