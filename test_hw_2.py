import unittest
from hw_2 import CustomClass

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.inst = CustomClass()

    def test_hasattr(self):
        self.assertEqual(hasattr(CustomClass, 'custom_x'), True)
        self.assertEqual(hasattr(CustomClass, 'custom_line'), True)
        self.assertEqual(hasattr(CustomClass, 'x'), False)
        self.assertEqual(hasattr(CustomClass, 'line'), False)

    def test_with_custom(self):
        self.assertEqual(self.inst.custom_x, 50)
        self.assertEqual(self.inst.custom_line(), 100)

    @unittest.expectedFailure
    def test_fail(self):
        self.fail(self.inst.x)
        self.fail(self.inst.line())


if __name__ == '__main__':
    unittest.main()
