from papagaio.main import resposta
import inspect
import pytest

def test_not_none():
    assert resposta(True, 10) is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(resposta(True, 13)) == bool, "Esperado um boleano"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"

def test_options_resposta():
    assert resposta(False, 13) == False , f"Esperado valor 'False'"
    assert resposta(True, 13) == False , f"Esperado valor 'False'"
    assert resposta(True, 6) == True , f"Esperado valor 'True'"
    assert resposta(True, 21) == True , f"Esperado valor 'True'"