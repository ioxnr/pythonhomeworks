for number in range(0, 21):
    if number == 2 or number == 3 or number == 4:
        print(number, 'процента')
    elif number == 0 or number >= 6:
        print(number, 'процентов')
    elif number == 1:
        print(number, 'процент')
