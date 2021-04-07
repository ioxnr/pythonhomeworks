class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        r1 = self.a * other.a
        r2 = (self.b * other.b) * -1

        i1 = self.a * other.b
        i2 = self.b * other.a

        real = r1 + r2
        imaginary = i1 + i2
        return ComplexNumber(real, imaginary)

    def __str__(self):
        if int(self.b) > 0:
            self.b = '+' + str(self.b)
        return f'{self.a} {self.b}i'


z1 = ComplexNumber(4, -3)
z2 = ComplexNumber(5, 7)
print(z1)
print(z1 + z2)
print(z1 * z2)
