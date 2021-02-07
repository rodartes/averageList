import unittest
import average

class TestAve(unittest.TestCase):
  def test1(self):
    self.assertEqual(average.averageList([1,2,3]), 2)
  def test2(self):
    self.assertEqual(average.averageList([-1, -2, -3]), -2)
  def test3(self):
    self.assertEqual(average.averageList([]), "Error")

if __name__ == '__main__':
  unittest.main()