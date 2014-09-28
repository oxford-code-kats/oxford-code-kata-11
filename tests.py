
import unittest

class TheTests(unittest.TestCase):
    def setUp(self):
        import sorter
        self.sorter = sorter.Sorter1(sorter.insert_slow)

    def test_list_of_one(self):
        self.sorter.add(1)
        self.assertEqual([1], self.sorter.as_list())

    def test_one_two(self):
        self.sorter.add(1)
        self.sorter.add(2)
        self.assertEqual([1, 2], self.sorter.as_list())

    def test_two_one(self):
        self.sorter.add(2)
        self.sorter.add(1)
        self.assertEqual([1, 2], self.sorter.as_list())

    def test_ten(self):
        self.sorter.add(1)
        self.sorter.add(10)
        self.sorter.add(2)
        self.sorter.add(3)
        self.sorter.add(4)
        self.sorter.add(5)
        self.sorter.add(6)
        self.sorter.add(7)
        self.sorter.add(8)
        self.sorter.add(9)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                self.sorter.as_list())


