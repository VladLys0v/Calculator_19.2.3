import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self,2,2) == 4

            # негативный тест
    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_devision_calculation_correctly(self):
        assert self.calc.division(self, 6, 2) == 3
    def test_substraction_calculated_correctly(self):
        assert self.calc.subtraction(self, 8, 3) == 5
    def test_adding_calculated_correctly(self):
        assert self.calc.adding(self, 8, 2) == 10