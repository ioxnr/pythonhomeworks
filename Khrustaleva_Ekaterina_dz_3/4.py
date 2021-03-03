from pprint import pprint


def thesaurus_adv(*names):
    result = {}
    for full_name in names:
        name, surname = full_name.split(' ')

        if surname[0] not in result:
            result[surname[0]] = {}

        if name[0] not in result[surname[0]]:
            result[surname[0]][name[0]] = []

        result[surname[0]][name[0]].append(full_name)

    return result


pprint(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
