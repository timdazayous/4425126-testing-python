import unittest

from calculate.operators import Operators

class TestAdditionOperator(unittest.TestCase):
    # addition
    def test_should_make_float_addition(self):
        sut = Operators()
        operation = "5.5 + 10"
        expected_value = 15.5
        self.assertEqual(sut.addition(operation), expected_value)

    def test_should_make_multiple_addition(self):
        sut = Operators()
        operation = "5 + 5 + 5"
        expected_value = 15
        self.assertEqual(sut.addition(operation), expected_value)
    
    def test_should_make_simple_addition(self):
        sut = Operators()
        operation = "5 + 10"
        expected_value = 15
        self.assertEqual(sut.addition(operation), expected_value)

    def test_should_make_negatives_addition(self):
        sut = Operators()
        operation = "5 + -10"
        expected_value = -5
        self.assertEqual(sut.addition(operation), expected_value)

    def test_random_spaces_addition(self):
        sut = Operators()
        operation = "   5+  7  "
        expected_value = 12
        self.assertEqual(sut.addition(operation), expected_value)

    def test_should_make_multiple_float_addition(self):
        sut = Operators()
        operation = "0.5 + 1.5 + 2.0 + 2.5"
        expected_value = 6.5
        self.assertEqual(sut.addition(operation), expected_value)

    def test_invalid_addition(self):
        sut = Operators()
        operation = "a + 2"
        expected_value = None
        self.assertEqual(sut.addition(operation), expected_value)

    def test_no_sign_addition(self):
        sut = Operators()
        operation = "42"
        expected_value = 42
        self.assertEqual(sut.addition(operation), expected_value)

    def test_no_sign2_addition(self):
        sut = Operators()
        operation = "4 2"
        expected_value = None
        self.assertEqual(sut.addition(operation), expected_value)

class TestSubstractionOperator(unittest.TestCase):
    # substraction
    def test_standard_substraction(self):
        sut = Operators()
        operation = "10 - 5"
        expected_value = 5
        self.assertEqual(sut.substraction(operation), expected_value)
    
    def test_multiple_substractio(self):
        sut = Operators()
        operation = "10 - 5 - 2"
        expected_value = 3
        self.assertEqual(sut.substraction(operation), expected_value)

    def test_float_substraction(self):
        sut = Operators()
        operation = "10.5 - 5"
        expected_value = 5.5
        self.assertEqual(sut.substraction(operation), expected_value)

    def test_negative_num_substraction(self):
        sut = Operators()
        operation = "10 - -5"
        expected_value = 15
        self.assertEqual(sut.substraction(operation), expected_value)

    def test_invalid_input_substraction(self):
        sut = Operators()
        operation = "10 - a"
        expected_value = None
        self.assertEqual(sut.substraction(operation), expected_value)

    def test_no_sign_substraction(self):
        sut = Operators()
        operation = "42"
        expected_value = 42
        self.assertEqual(sut.substraction(operation), expected_value)

class TestMultiplicationOperator(unittest.TestCase):
    # multiplication
    def test_standard_multiplication(self):
        sut = Operators()
        operation = "4 * 2"
        expected_value = 8
        self.assertEqual(sut.multiplication(operation), expected_value)

    def test_multiple_multiplication(self):
        sut = Operators()
        operation = "4 * 2 * 2"
        expected_value = 16
        self.assertEqual(sut.multiplication(operation), expected_value)

    def test_float_multiplication(self):
        sut = Operators()
        operation = "4.2 * 2"
        expected_value = 8.4
        self.assertEqual(sut.multiplication(operation), expected_value)
    
    def test_by_zero_multiplication(self):
        sut = Operators()
        operation = "4 * 0"
        expected_value = 0
        self.assertEqual(sut.multiplication(operation), expected_value)

    ## to be coninued ...

class TestDivisionOperator(unittest.TestCase):
    # division
    def test_should_make_division(self):
        sut = Operators()
        operation = "4 / 2"
        expected_value = 2
        self.assertEqual(sut.division(operation), expected_value)

    def test_should_not_make_by_0_division(self):
        sut = Operators()
        operation = "4 / 0"
        expected_value = None
        self.assertEqual(sut.division(operation), expected_value)

    def test_should_make_float_division(self):
        sut = Operators()
        operation = "4.2 / 2"
        expected_value = 2.1
        self.assertEqual(sut.division(operation), expected_value)

    # to be coninued ...



if __name__ == "__main__":
    unittest.main()

