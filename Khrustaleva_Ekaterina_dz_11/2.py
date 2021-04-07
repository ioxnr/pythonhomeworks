class Division:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    def divide(self):
        if self.divider == 0:
            raise ZeroDivisionErrorException
        else:
            return self.dividend / self.divider


class ZeroDivisionErrorException(Exception):

    def __str__(self):
        return 'Делить на ноль недопустимо'


div1 = Division(10, 0)
div2 = Division(10, 5)

try:
    print(div1.divide())
except ZeroDivisionErrorException as exception:
    print(exception)

try:
    print(div2.divide())
except ZeroDivisionErrorException as exception:
    print(exception)
