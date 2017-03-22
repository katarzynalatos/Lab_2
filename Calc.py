from AbstractCalc import AbstractCalc
from Validator import Validator
from sympy import diff


class Calc(AbstractCalc):
    def add(self, first, second):
        add_validate = Validator(first, second, "add")
        add_validate.validate()
        return first + second

    def divide(self, numerator, denominator):
        divide_validate = Validator(numerator, denominator, "divide")
        divide_validate.validate()
        return numerator/denominator

    def derivative(self, function, degree):
        derivative_validate = Validator(0, degree, "derivative", function)
        derivative_validate.validate()
        return diff(function, 'x**2', degree)




