import pytest
from main import soma


class TestMain():
    def test_soma_1(self):
        assert soma(1, 3) == 4

    def test_soma_2(self):
        assert soma(1, 2) is not 2
