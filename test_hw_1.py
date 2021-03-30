import unittest
from hw_1 import CustomList


class MyTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(CustomList.__add__(CustomList([1, -5, 8]),
                                            [1, -5, 8, 9]), [2, -10, 16, 9])
        self.assertEqual(CustomList.__add__(CustomList([1, -5, 8, 9]),
                                            [1, -5, 8, 9]), [2, -10, 16, 18])
        self.assertEqual(CustomList.__add__(CustomList([1, -5, 8, 9]),
                                            [1, -5, 8]), [2, -10, 16, 9])
        self.assertEqual(CustomList.__add__(CustomList([1, -5, 8]),
                                            CustomList([1, -5, 8, 9])), [2, -10, 16, 9])
        self.assertEqual(CustomList.__add__(CustomList([1, -5, 8, 9]),
                                            CustomList([1, -5, 8, 9])), [2, -10, 16, 18])
        self.assertEqual(CustomList.__add__(CustomList([1, -5, 8, 9]),
                                            CustomList([1, -5, 8])), [2, -10, 16, 9])

    def test_radd(self):
        self.assertEqual(CustomList.__radd__(CustomList([1, -5, 8]),
                                             [1, -5, 8, 9]), [2, -10, 16, 9])
        self.assertEqual(CustomList.__radd__(CustomList([1, -5, 8, 9]),
                                             [1, -5, 8, 9]), [2, -10, 16, 18])
        self.assertEqual(CustomList.__radd__(CustomList([1, -5, 8, 9]),
                                             [1, -5, 8]), [2, -10, 16, 9])

    def test_sub(self):
        self.assertEqual(CustomList.__sub__(CustomList([1, -5, 8]),
                                            [1, -5, 8, 9]), [0, 0, 0, -9])
        self.assertEqual(CustomList.__sub__(CustomList([1, -5, 8, 9]),
                                            [1, -5, 8, 9]), [0, 0, 0, 0])
        self.assertEqual(CustomList.__sub__(CustomList([1, -5, 8, 9]),
                                            [1, -5, 8]), [0, 0, 0, 9])
        self.assertEqual(CustomList.__sub__(CustomList([1, -5, 8]),
                                            CustomList([1, -5, 8, 9])), [0, 0, 0, -9])
        self.assertEqual(CustomList.__sub__(CustomList([1, -5, 8, 9]),
                                            CustomList([1, -5, 8, 9])), [0, 0, 0, 0])
        self.assertEqual(CustomList.__sub__(CustomList([1, -5, 8, 9]),
                                            CustomList([1, -5, 8])), [0, 0, 0, 9])

    def test_rsub(self):
        self.assertEqual(CustomList.__rsub__(CustomList([1, -5, 8]),
                                             [1, -5, 8, 9]), [0, 0, 0, 9])
        self.assertEqual(CustomList.__rsub__(CustomList([1, -5, 8, 9]),
                                             [1, -5, 8, 9]), [0, 0, 0, 0])
        self.assertEqual(CustomList.__rsub__(CustomList([1, -5, 8, 9]),
                                             [1, -5, 8]), [0, 0, 0, -9])

    def test_lt(self):
        self.assertEqual(CustomList.__lt__(CustomList([1, -5, 8]),
                                           [1, -5, 8, 9]), True)
        self.assertEqual(CustomList.__lt__(CustomList([1, -5, 8, 9]),
                                           [1, -5, 8, 9]), False)
        self.assertEqual(CustomList.__lt__(CustomList([1, -5, 8]),
                                           CustomList([1, -5, 8, 9])), True)
        self.assertEqual(CustomList.__lt__(CustomList([1, -5, 8, 9]),
                                           CustomList([1, -5, 8, 9])), False)

    def test_le(self):
        self.assertEqual(CustomList.__le__(CustomList([1, -5, 8]),
                                           [1, -5, 8, 9]), True)
        self.assertEqual(CustomList.__le__(CustomList([1, -5, 8, 9]),
                                           [1, -5, 8, 9]), True)
        self.assertEqual(CustomList.__le__(CustomList([1, -5, 8, 10]),
                                           [1, -5, 8, 9]), False)
        self.assertEqual(CustomList.__le__(CustomList([1, -5, 8]),
                                           CustomList([1, -5, 8, 9])), True)
        self.assertEqual(CustomList.__le__(CustomList([1, -5, 8, 9]),
                                           CustomList([1, -5, 8, 9])), True)
        self.assertEqual(CustomList.__le__(CustomList([1, -5, 8, 10]),
                                           CustomList([1, -5, 8, 9])), False)

    def test_gt(self):
        self.assertEqual(CustomList.__gt__(CustomList([1, -5, 8, 9]),
                                           [1, -5, 8]), True)
        self.assertEqual(CustomList.__gt__(CustomList([1, -5, 8, 9]),
                                           [1, -5, 8, 9]), False)
        self.assertEqual(CustomList.__gt__(CustomList([1, -5, 8, 9]),
                                           CustomList([1, -5, 8])), True)
        self.assertEqual(CustomList.__gt__(CustomList([1, -5, 8, 8]),
                                           CustomList([1, -5, 8, 9])), False)

    def test_ge(self):
        self.assertEqual(CustomList.__ge__(CustomList([1, -5, 8, 9]),
                                           [1, -5, 8]), True)
        self.assertEqual(CustomList.__ge__(CustomList([1, -5, 8, 9]),
                                           [1, -5, 8, 9]), True)
        self.assertEqual(CustomList.__ge__(CustomList([1, -5, 8]),
                                           [1, -5, 8, 9]), False)
        self.assertEqual(CustomList.__ge__(CustomList([1, -5, 8, 10]),
                                           CustomList([1, -5, 8, 9])), True)
        self.assertEqual(CustomList.__ge__(CustomList([1, -5, 8, 9]),
                                           CustomList([1, -5, 8, 9])), True)
        self.assertEqual(CustomList.__ge__(CustomList([1, -5, 8]),
                                           CustomList([1, -5, 8, 9])), False)

    def test_eq(self):
        self.assertEqual(CustomList.__eq__(CustomList([1, -5, 8, 9]),
                                           [1, -5, 8, 9]), True)
        self.assertEqual(CustomList.__eq__(CustomList([1, -5, 8]),
                                           [1, -5, 8, 9]), False)
        self.assertEqual(CustomList.__eq__(CustomList([1, -5, 8, 9]),
                                           CustomList([1, -5, 8, 9])), True)
        self.assertEqual(CustomList.__eq__(CustomList([1, -5, 8]),
                                           CustomList([1, -5, 8, 9])), False)

    def test_ne(self):
        self.assertEqual(CustomList.__ne__(CustomList([1, -5, 8, 9]),
                                           [1, -5, 8, 9]), False)
        self.assertEqual(CustomList.__ne__(CustomList([1, -5, 8]),
                                           [1, -5, 8, 9]), True)
        self.assertEqual(CustomList.__ne__(CustomList([1, -5, 8, 9]),
                                           CustomList([1, -5, 8, 9])), False)
        self.assertEqual(CustomList.__ne__(CustomList([1, -5, 8]),
                                           CustomList([1, -5, 8, 9])), True)


if __name__ == '__main__':
    unittest.main()
