class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join([' '.join([str(j) for j in i]) for i in self.lists])

    def __add__(self, other):
        result = []
        for sublist in zip(self.lists, other.lists):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            result.append(temp)
        return '\n'.join([' '.join([str(j) for j in i]) for i in result])


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[45, 67, 100], [44, 12, 90], [32, 87, 10]])
print(m1)
print(m2)
print(m1 + m2)
m3 = Matrix([[31, 22], [37, 43], [51, 86]])
m4 = Matrix([[44, 58], [20, 11], [10, 12]])
print(m3)
print(m4)
print(m3 + m4)
