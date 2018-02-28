import unittest

class TDDInPython(unittest.TestCase):

    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(5,17)
        self.assertEqual(22, result)

if __name__ == '__main__':
    unittest.main()

