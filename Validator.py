from AbstractValidator import AbstractValidator
import Exceptions


class Validator(AbstractValidator):
    def __init__(self, to_validate_first, to_validate_second, action, to_derivative_str=""):
        super(Validator, self).__init__()
        self._to_validate_first = to_validate_first
        self._to_validate_second = to_validate_second
        self._action = action
        self._to_derivative_str=to_derivative_str

    def validate(self):
        if self._is_number(self._to_validate_first) and self._is_number(self._to_validate_second):
            if self._action=="divide" and self._is_a_zero(self._to_validate_second):
                raise Exceptions.IsZero
            if self._action=="derivative" and self._is_not_more_or_equal_zero(self._to_validate_second):
                raise Exceptions.NotHigherAndEqualZero
            if self._action=="derivative" and self._is_not_a_string(self._to_derivative_str):
                raise Exceptions.NotAString
            else:
                return True
        else:
            raise Exceptions.NotANumber

    @staticmethod
    def _is_number( number):
        if isinstance(number, int):
            return True
        elif isinstance(number, float):
            return True
        else:
            return False

    @staticmethod
    def _is_a_zero(number):
        if number>-1E-10 and number<1E-10:
            return True
        else:
            return False

    @staticmethod
    def _is_not_more_or_equal_zero(number):
        if number >= 0:
            return False
        else:
            return True

    @staticmethod
    def _is_not_a_string(string):
        if isinstance(string, str):
            return False
        else:
            return True

