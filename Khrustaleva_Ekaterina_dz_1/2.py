cubes = []


def sum_digits(value):
    result = 0

    while value != 0:
        result += value % 10
        value //= 10

    return result


for i in range(0, 1001):
    if (i ** 3) % 2 != 0:
        cubes.append(i ** 3)

res_1 = sum(filter(lambda number: sum_digits(number) % 7 == 0, cubes))
res_2 = sum(filter(lambda number: sum_digits(number + 17) % 7 == 0, cubes))

print(res_1)
print(res_2)
