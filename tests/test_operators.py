from calculate.operators import Operators

# test d'addition
def test_should_make_multiple_addition():
    # Création d'un objet de la classe operator pour pouvoir y appliquer ses fonctions
    sut = Operators()
    operation = "5.5 + 10 + 30 + 13.7"
    expected_value = 59.2
    assert sut.addition(operation) == expected_value

def test_make_simple_addition():
    sut = Operators()
    operation = "10 + 5"
    expected_value = 15
    assert sut.addition(operation) == expected_value

# Ce qu'il devrait se passer
def test_should_negatives_numbers_addition():
    sut = Operators()
    operation = "5 + -4 + -1"
    expected_value = 0
    assert sut.addition(operation) == expected_value
# Etat actuel
def test_negatives_numbers_addition():
    sut = Operators()
    operation = "5 + -4 + -1"
    expected_value = None
    assert sut.addition(operation) == expected_value

def test_random_spaces_addition():
    sut = Operators()
    operation = "   5+  7  "
    expected_value = 12
    assert sut.addition(operation) == expected_value

def test_should_make_float_addition():
    sut = Operators()
    operation = "0.5 + 1.5"
    expected_value = 2
    assert sut.addition(operation) == expected_value

def test_should_make_multiple_float_addition():
    sut = Operators()
    operation = "0.5 + 1.5 + 2.0 + 2.5"
    expected_value = 6.5
    assert sut.addition(operation) == expected_value

def test_invalid_addition():
    sut = Operators()
    operation = "a + 2"
    expected_value = None
    assert sut.addition(operation) == expected_value

def test_no_sign_addition():
    sut = Operators()
    operation = "42"
    expected_value = 42.0
    assert sut.addition(operation) == expected_value

def test_no_sign2_addition():
    sut = Operators()
    operation = "4 2"
    expected_value = None
    assert sut.addition(operation) == expected_value

# test substraction
def test_standard_substraction():
    sut = Operators()
    operation = "10 - 5"
    expected_value = 5
    assert sut.substraction(operation) == expected_value

def test_multiple_substraction():
    sut = Operators()
    operation = "10 - 5 - 3"
    expected_value = 2
    assert sut.substraction(operation) == expected_value

def test_float_substraction():
    sut = Operators()
    operation = "10.5 - 5.5"
    expected_value = 5
    assert sut.substraction(operation) == expected_value

def test_negative_num_substraction():
    sut = Operators()
    operation = "10 - -5"
    expected_value = 15
    assert sut.substraction(operation) == expected_value

def test_invalid_input_substraction():
    sut = Operators()
    operation = "10 - abc"
    expected_value = None
    assert sut.substraction(operation) == expected_value

def test_no_sign_substraction():
    sut = Operators()
    operation = "42"
    expected_value = 42.0
    assert sut.substraction(operation) == expected_value

# test multiplication
def test_standard_multiplication():
    sut = Operators()
    operation = "10 * 5"
    expected_value = 50
    assert sut.multiplication(operation) == expected_value

def test_multiple_multiplication():
    sut = Operators()
    operation = "10 * 5 * 2"
    expected_value = 100
    assert sut.multiplication(operation) == expected_value

def test_float_multiplication():
    sut = Operators()
    operation = "2.5 * 4"
    expected_value = 10
    assert sut.multiplication(operation) == expected_value

def test_by_zero_multiplication():
    sut = Operators()
    operation = "10 * 0 * 2"
    expected_value = 0
    assert sut.multiplication(operation) == expected_value

def test_invalid_input_multiplication():
    sut = Operators()
    operation = "10 * abc"
    expected_value = None
    assert sut.multiplication(operation) == expected_value

def test_no_sign_multiplication():
    sut = Operators()
    operation = "105"
    expected_value = 105
    assert sut.multiplication(operation) == expected_value

def test_solo_multiplication():
    sut = Operators()
    operation = "10"
    expected_value = 10
    assert sut.multiplication(operation) == expected_value

# test division
def test_simple_division():
    sut = Operators()
    operation = "10 / 5"
    expected_value = 2
    assert sut.division(operation) == expected_value

def test_simple_2_division():
    sut = Operators()
    operation = "10/5"
    expected_value = 2
    assert sut.division(operation) == expected_value

def test_multiple_division():
    sut = Operators()
    operation = "10 / 2 / 2"
    expected_value = 2.5
    assert sut.division(operation) == expected_value

def test_float_division():
    sut = Operators()
    operation = "2.4 / 2"
    expected_value = 1.2
    assert sut.division(operation) == expected_value

def test_float_2_division():
    sut = Operators()
    operation = "10 / 2.5"
    expected_value = 4
    assert sut.division(operation) == expected_value

def test_by_zero_division():
    sut = Operators()
    operation = "10 / 0"
    expected_value = None
    assert sut.division(operation) == expected_value

def test_solo_division():
    sut = Operators()
    operation = "10"
    expected_value = 10
    assert sut.division(operation) == expected_value

def test_invalid_input_division():
    sut = Operators()
    operation = "10 / abc"
    expected_value = None
    assert sut.division(operation) == expected_value