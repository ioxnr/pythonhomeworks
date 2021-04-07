class OnlyNumbersException(Exception):

    def __str__(self):
        return 'Недопустимое значение, введите число'


numbers = []

while True:
    try:
        value = input('Введите число: ')
        if value == 'stop':
            print(f'\n{numbers}')
            break
        try:
            numbers.append(int(value))
        except ValueError:
            raise OnlyNumbersException
    except OnlyNumbersException as exception:
        print(exception)
