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

    