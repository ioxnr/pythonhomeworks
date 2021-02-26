employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']

new_list = []

for i in range(len(employees)):
    new_list.append(employees[i].split(' '))

for i in range(len(new_list)):
    print('Привет,', new_list[i][-1].capitalize())
