import pytest
from calculadora import Calculadora


class TesteCalculadora():

    def setup(self):
        self.calculadora = Calculadora(3, 3)

    def test_health(self):
        assert self.calculadora.health() == "OK"

    def test_soma(self):
        resultado = self.calculadora.soma()
        assert resultado == (self.calculadora.num_1 + self.calculadora.num_2)

    def test_subtracao(self):
        resultado = self.calculadora.subtracao()
        assert resultado == (self.calculadora.num_1 - self.calculadora.num_2)

    def test_multiplicacao(self):
        resultado = self.calculadora.multiplicacao()
        assert resultado == (self.calculadora.num_1 * self.calculadora.num_2)

    def test_divisao(self):
        resultado = self.calculadora.divisao()
        assert resultado == (self.calculadora.num_1 / self.calculadora.num_2)
