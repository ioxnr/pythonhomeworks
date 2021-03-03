from pprint import pprint


def thesaurus(*name):
    for i in name:
        if i[0] not in names.keys():
            names[i[0]] = []
            names[i[0]].append(i)
        else:
            names[i[0]].append(i)


names = {}

thesaurus("Иван", "Мария", "Петр", "Илья")

pprint(names)
