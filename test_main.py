import pytest
from main import soma, subtracao, multiplicacao, divisao


class TestMain():
    def test_soma(self):
        assert soma(1, 3) == 4

    def test_subtracao(self):
        assert subtracao(2, 1) == 1

    def test_multiplicacao(self):
        assert multiplicacao(2, 2) == 4

    def test_divisao(self):
        assert divisao(2, 1) == 2
