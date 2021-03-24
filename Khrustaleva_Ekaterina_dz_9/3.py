class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


test_worker = Position('Andrew', 'Bogatov', 'accountant', 20000, 5000)
print(test_worker.name)
print(test_worker.get_full_name())
print(test_worker.get_total_income())
