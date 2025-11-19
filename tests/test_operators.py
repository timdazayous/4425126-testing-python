from calculate.operators import Operators

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