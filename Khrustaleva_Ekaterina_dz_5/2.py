from itertools import islice

n = int(input("Введите любое число: "))

odd_nums = (num for num in range(1, n + 1, 2))

print(*islice(odd_nums, n))
