class Road:
    _length: float
    _width: float
    _asphalt_mass: float

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self._asphalt_mass = 25.0

    def weight(self, thickness: float = 1):
        return (self._length * self._width * self._asphalt_mass * thickness) / 1000


mass = Road(20, 5000)
print(mass.weight(5))
