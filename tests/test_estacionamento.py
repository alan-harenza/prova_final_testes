"""Controle de Estacionamento feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
import pytest
from app.estacionamento import Estacionamento
from app.ticket import Ticket


@scenario('tests\estacionamento.feature', 'calcular o valor devido para a saida de veiculo')
def test_calcular_o_valor_devido_para_a_saida_de_veiculo():
    """calcular o valor devido para a saida de veiculo."""


@given('um veiculo esta estacionado ha 2 horas')
def _():
    """um veiculo esta estacionado ha 2 horas."""
    raise NotImplementedError


@when('o cliente apresenta o ticket de entrada para a saida')
def _():
    """o cliente apresenta o ticket de entrada para a saida."""
    raise NotImplementedError


@then('o frentista calcula o valor devido corretamente')
def _():
    """o frentista calcula o valor devido corretamente."""
    raise NotImplementedError


@scenario('tests\estacionamento.feature', 'emitir um ticket para entrada de veiculo')
def test_emitir_um_ticket_para_entrada_de_veiculo():
    """emitir um ticket para entrada de veiculo."""


@given('um veiculo entra no Estacionamento')
def _():
    """um veiculo entra no Estacionamento."""
    raise NotImplementedError


@when('o frentista emite um ticket para o veiculo')
def _():
    """o frentista emite um ticket para o veiculo."""
    raise NotImplementedError


@then('o ticket contem informacoes corretas sobre a entrada do veiculo')
def _():
    """o ticket contem informacoes corretas sobre a entrada do veiculo."""
    raise NotImplementedError
