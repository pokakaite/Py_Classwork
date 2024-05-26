import unittest
import module

class Test_calculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = module.Calculator()

    def testAdd(self):
        self.assertEqual(self.calc.add(1, 1), 2)

    def testMul(self):
        self.assertEqual(self.calc.mul(1, 1), 1)

    def testDiv(self):
        self.assertEqual(self.calc.div(1, 1), 1)

    def testSubstract(self):
        self.assertEqual(self.calc.subtract(1, 1), 0)


if __name__ == '__main__':
    print(__name__)
    unittest.main()