import pytest
from src.pgrm import Calculator

class TestCalculator:
    @pytest.fixture()
    def calc(self):
        return Calculator()

    def test_sum(self,calc):
        assert calc.add(3, 5) ==8

    def test_upper_fail(self,calc):
        assert calc.to_upper("hello") == "hello"

    @pytest.fixture()
    def number_list(self,calc):
        return calc.get_numbers()

    def test_list_length(self,number_list):
        assert len(number_list) == 3

    @pytest.mark.parametrize("input,expected",[
        (2,4),
        (3,9),
        (4,16)
    ])
    def test_square(self,calc,input,expected):
        assert calc.square(input) == expected

    def test_zero_division(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.divide(10,0)