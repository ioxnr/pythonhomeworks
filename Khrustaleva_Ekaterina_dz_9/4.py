class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'The {self.name} is going')

    def stop(self):
        print(f'The {self.name} has stopped')

    def turn(self, direction):
        print(f'The {self.name} has turned {direction}')

    def show_speed(self):
        print(f'{self.name} current speed is - {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Speed exceeded')


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Speed exceeded')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


audi = Car(70, 'white', 'Audi')
bmw = TownCar(120, 'black', 'BMW')
ford = SportCar(130, 'yellow', 'Ford')
nissan = WorkCar(80, 'red', 'Nissan')
lada = PoliceCar(60, 'grey', 'Lada')

print(f'The color of {audi.name} - {audi.color}')
print(f'{ford.name} speed is {ford.speed}')
print(f'Is {lada.name} a police car? - {lada.is_police}')
nissan.show_speed()
bmw.show_speed()
lada.go()
ford.stop()
bmw.turn('left')
