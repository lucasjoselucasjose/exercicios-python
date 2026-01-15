from data_segundos.main import resposta
import inspect
import pytest

def test_not_none():
    assert resposta(4) is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(resposta(4)) == int, "Esperado um inteiro"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 4, "Assinatura da função deverá receber quatro parâmetros"

def test_options_resposta():
    assert resposta(10, 10, 10, 10) == 900610 , f"Esperado valor 900610"
    assert resposta(25, 1, 45, 20 ) == 2166320 , f"Esperado valor 2166320"
