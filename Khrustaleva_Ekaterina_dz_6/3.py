import json

users = []
hobbies = []

with open('users.csv', 'r', encoding='utf-8') as users_file:
    for line in users_file:
        users.append(line.replace('\n', '').replace(',', ' '))

with open('hobby.csv', 'r', encoding='utf-8') as hobbies_file:
    for line in hobbies_file:
        hobbies.append(line.replace('\n', '').split(','))

users_hobbies = dict(zip(users, hobbies))

delta = len(users) - len(hobbies)
if delta < 0:
    exit(1)

hobbies += [None] * delta

users_hobbies = dict(zip(users, hobbies))

with open('users_hobbies.json', 'w', encoding='utf-8') as users_hobbies_file:
    data = json.dumps(users_hobbies)
    users_hobbies_file.write(data)

with open('users_hobbies.json', encoding='utf-8') as users_hobbies_file2:
    opened_file = json.loads(users_hobbies_file2.read())
    print(opened_file)
