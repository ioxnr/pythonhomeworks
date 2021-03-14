from itertools import islice
from sys import argv

if __name__ == '__main__':
    args = argv[1:]

if len(args) == 0:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
elif len(args) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in islice(f, int(args[0]) - 1, None):
            print(line)
elif len(args) == 2:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in islice(f, int(args[0]) - 1, int(args[1])):
            print(line)
