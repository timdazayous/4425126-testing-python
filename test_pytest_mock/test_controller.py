from calculate.operators import Operators
from calculate.view import View

from calculate.controller import Controller

def test_quit_without_infinite_loop(mocker):
    sut = Controller()
    mock = mocker.patch('calculate.view.view.get_user_input', return_value = 5)


def test_addition(mocker):
    expected_value = 1.0
    sut = Controller()
    mock = mocker.patch('calculate.view.View.get_user_input')
    
    mock.side_effect = ["1", "10+10","5"] # suite d'input envoyé par le mock pour chaques appel successif de get_user_input
    # appel 1 on simule un input de "1" (choix addition dasn le menu)
    # appel 2 on simule l'input "10+10" addition que l'on souhaite tester
    # appel 3 on simule l'input de "5" pour quitter le menu 

    mocker.patch('calculate.operators.Operators.addition', return_value = expected_value) # Ne fait rien retourne juste expected_value
    mocker.patch('calculate.view.View.continue_message') # Ne fait rien 

    sut.run() # appel Operators.addition("10+10") mais grace au mock retouren directement 1
    assert sut.result == expected_value

def test_substraction(mocker):
    expected_value = 5
    sut = Controller()
    mock = mocker.patch('calculate.view.View.get_user_input')

    mock.side_effect = ["2", "10-5", "5"]

    mocker.patch('calculate.view.View.Operators.substraction', return_value = expected_value)
    mocker.patch('calculate.view.View.continue_message')

    sut.run()
    assert sut.result == expected_value

