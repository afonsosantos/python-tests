import pytest
from main import soma


class TestMain():
    def test_soma_1(self):
        assert soma(1, 3) == 4
