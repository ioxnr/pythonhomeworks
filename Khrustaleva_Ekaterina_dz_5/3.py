from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б'
]

classes_gen = (i for i in zip_longest(tutors, klasses, fillvalue=None))
print(classes_gen)
print(next(classes_gen))
print(next(classes_gen))
print(next(classes_gen))
print(next(classes_gen))
print(next(classes_gen))
print(next(classes_gen))
print(next(classes_gen))
print(next(classes_gen))
print(next(classes_gen))
