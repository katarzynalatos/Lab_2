import abc


class AbstractCalc(object, metaclass=abc.ABCMeta):
    def add(self, first, second):
        pass

    def divide(self, numerator, denominator):
        pass

    def derivative(self, function, degree):
        pass
