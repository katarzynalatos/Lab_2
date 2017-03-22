from Calc import Calc
from unittest import TestCase
from unittest.mock import patch
import Exceptions
import unittest


class TestCalc(TestCase):
#add
    def test_correct_adding__two_integers(self):
        c = Calc()
        first = 20
        second = 25
        expected_result = 45
        self.assertEqual(expected_result, c.add(first, second))

    def test_correct_adding_two_floats(self):
        c = Calc()
        first = 20.3
        second = 25.9
        expected_result = 46.2
        self.assertAlmostEqual(expected_result, c.add(first, second))

    def test_correct_adding_float_and_integer(self):
        c = Calc()
        first = 20.3
        second = 25
        expected_result = 45.3
        self.assertAlmostEqual(expected_result, c.add(first, second))

    def test_correct_adding_integer_and_float(self):
        c = Calc()
        first = 20
        second = 25.3
        expected_result = 45.3
        self.assertAlmostEqual(expected_result, c.add(first, second))

    def test_correct_adding_string_and_string_(self):
        c = Calc()
        first = "+"
        second = "+"
        self.assertRaises(Exceptions.NotANumber, c.add, first, second)

    def test_correct_adding_string_and_not_string_(self):
        c = Calc()
        first = "+"
        second = 1.3
        self.assertRaises(Exceptions.NotANumber, c.add, first, second)

    def test_correct_adding_not_string_and_string(self):
        c = Calc()
        first = 1
        second = "+"
        self.assertRaises(Exceptions.NotANumber, c.add, first, second)

#---------------------------------------------------------------------------------------
#divide
    def test_correct_divide_two_integers(self):
        c = Calc()
        first = 5
        second = 2
        expected_result = 2.5
        self.assertAlmostEqual(expected_result, c.divide(first, second))

    def test_correct_divide_two_floats(self):
        c = Calc()
        first = 8.5
        second = 2.5
        expected_result = 3.4
        self.assertAlmostEqual(expected_result, c.divide(first, second))

    def test_correct_divide_float_and_integer(self):
        c = Calc()
        first = 8.5
        second = 2
        expected_result = 4.25
        self.assertAlmostEqual(expected_result, c.divide(first, second))

    def test_correct_divide_integer_and_float(self):
        c = Calc()
        first = 8
        second = 2.5
        expected_result = 3.2
        self.assertAlmostEqual(expected_result, c.divide(first, second))

    def test_correct_divide_number_and_float_zero(self):
        c = Calc()
        first = 8
        second = 0
        self.assertRaises(Exceptions.IsZero, c.divide, first, second)

    def test_correct_divide_number_and_integer_zero(self):
        c = Calc()
        first = 8
        second = 0.0
        self.assertRaises(Exceptions.IsZero, c.divide, first, second)

    def test_correct_divide_string_and_string_(self):
        c = Calc()
        first = "+"
        second = "+"
        self.assertRaises(Exceptions.NotANumber, c.divide, first, second)

#---------------------------------------------------------------------------------------------------------------
#derivative

    def test_correct_derivative_string_and_string_(self):
        c = Calc()
        first = "x**2"
        second = "xss"
        self.assertRaises(Exceptions.NotANumber, c.derivative, first, second)

    def test_correct_derivative_string_and_not_int_(self):
        c = Calc()
        first = "x**2"
        second = 1.2
        self.assertRaises(Exceptions.NotInteger, c.derivative, first, second)

    def test_correct_derivative_string_and_less_than_zero_int_(self):
        c = Calc()
        first = "x**2"
        second = -1
        self.assertRaises(Exceptions.NotHigherAndEqualZero, c.derivative, first, second)

    @patch('Calc.Calc.derivative')
    def test_correct_derivative_str_and_integer(self, mock):
        mock.return_value = "2*x"
        c = Calc()
        first = "x**2"
        second = 1
        expected_result = "2*x"
        self.assertEqual(expected_result, c.derivative(first, second))

if __name__ == "__main__":
    unittest.main()
    
