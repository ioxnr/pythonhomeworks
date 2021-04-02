class Cell:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'Результат операции равен {self.amount}'

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            return Cell(self.amount - other.amount)
        else:
            return 'Разность количества ячеек двух клеток должна быть больше нуля'

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __floordiv__(self, other):
        return Cell(round(self.amount // other.amount))

    def __truediv__(self, other):
        return Cell(round(self.amount / other.amount))

    def make_order(self, amount_in_row):
        row = ''
        for i in range(int(self.amount / amount_in_row)):
            row += '*' * amount_in_row + '\n'
        row += '*' * (self.amount % amount_in_row)
        return row


c = Cell(56)
b = Cell(20)
print(c + b)
print(c - b)
print(c * b)
print(c // b)
print(c / b)
print(c.make_order(6))
print(b.make_order(5))
