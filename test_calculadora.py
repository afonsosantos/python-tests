import pytest
from random import randint
from calculadora import Calculadora


class TestesCalculadora:

    def setup(self):
        self.calculadora = Calculadora(randint(1, 100), randint(1, 100))
        self.resultado = 0

    def test_soma(self):
        self.resultado = self.calculadora.soma()
        assert self.resultado == (
            self.calculadora.num_1 + self.calculadora.num_2)

    def test_subtracao(self):
        self.resultado = self.calculadora.subtracao()
        assert self.resultado == (
            self.calculadora.num_1 - self.calculadora.num_2)

    def test_multiplicacao(self):
        self.resultado = self.calculadora.multiplicacao()
        assert self.resultado == (
            self.calculadora.num_1 * self.calculadora.num_2)

    def test_divisao(self):
        self.resultado = self.calculadora.divisao()
        assert self.resultado == (
            self.calculadora.num_1 / self.calculadora.num_2)

    def test_divisao_zero(self):
        self.calculadora = Calculadora(0, 2)
        self.resultado = self.calculadora.divisao()
        assert self.resultado == 'Divisão por Zero'


if __name__ == '__main__':
    pytest.main(args=[__file__])
