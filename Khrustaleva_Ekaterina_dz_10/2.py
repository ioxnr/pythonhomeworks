from abc import ABC, abstractmethod


class Textile(ABC):

    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def consumption(self):
        pass


class Coat(Textile):

    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    @property
    def consumption(self):
        return self._size / 6.5 + 0.5


class Suit(Textile):

    def __init__(self, name, height):
        super().__init__(name)
        self._height = height

    @property
    def consumption(self):
        return 2 * self._height + 0.3


garments = [Coat('Bat Norton Dementor', 5), Suit('Gucci', 6)]
for garment in garments:
    print(garment.consumption)
total_consumption = sum(g.consumption for g in garments)
print(total_consumption)
