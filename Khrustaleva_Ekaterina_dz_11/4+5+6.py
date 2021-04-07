class Stock:
    def __init__(self):
        self.equipment = {'printers': 0, 'scanners': 0, 'copiers': 0}

    def acceptance(self, article):
        if isinstance(article, Printer):
            self.equipment['printers'] += 1
        elif isinstance(article, Scanner):
            self.equipment['scanners'] += 1
        elif isinstance(article, Copier):
            self.equipment['copiers'] += 1
        return 'Товар был принят на склад'


class OfficeEquipment:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Printer(OfficeEquipment):

    def __init__(self, name, quantity, price, number_of_cartridges):
        super().__init__(name, quantity, price)
        self.number_of_cartridges = number_of_cartridges


class Scanner(OfficeEquipment):

    def __init__(self, name, quantity, price, capacity):
        super().__init__(name, quantity, price)
        self.capacity = capacity


class Copier(OfficeEquipment):

    def __init__(self, name, quantity, price, amount_of_paper):
        super().__init__(name, quantity, price)
        self.amount_of_paper = amount_of_paper


unit_1 = Printer('hp', 5, 2000, 10)
unit_2 = Scanner('Canon', 3, 1200, 100)
unit_3 = Copier('Xerox', 2, 1500, 150)

stock = Stock()
print(stock.acceptance(unit_1))
print(stock.acceptance(unit_2))
print(stock.acceptance(unit_3))
print(stock.equipment)
