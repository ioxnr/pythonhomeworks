from time import sleep


class TrafficLight:
    __color: list

    def __init__(self):
        self.__color = ['Red', 'Yellow', 'Green']

    def running(self):
        counter = 0
        while counter < 3:
            if counter == 0:
                print(self.__color[counter])
                sleep(7)
            elif counter == 1:
                print(self.__color[counter])
                sleep(2)
            else:
                print(self.__color[counter])
                sleep(7)
            counter += 1


TrafficLightTest = TrafficLight()
TrafficLightTest.running()
