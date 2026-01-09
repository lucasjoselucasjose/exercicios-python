from soma_num_int.main import resposta
import inspect
import pytest

def test_not_none():
    assert resposta(10, 3) is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(resposta(10, 3)) == int, "Esperado um inteiro"

def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"

def test_options_resposta():
    assert resposta(3.3, 7) == 10 , f"Esperado valor 10"
    assert resposta(15.9, 15) == 30, f"Esperado valor 30"
    assert resposta(0, 2) == 2, f" Esperando 2"