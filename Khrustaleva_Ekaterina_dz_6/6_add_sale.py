from sys import argv

if __name__ == '__main__':
    values = [i + '\n' for i in argv[1:]]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.writelines(values)
