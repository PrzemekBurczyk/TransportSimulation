from pygame import image
from transport.transporter import Transporter
from random import randint


class Taxi(Transporter):
    taxi_capacity = 3
    taxi_speed = 10

    def __init__(self, position, city, speed=None):
        Transporter.__init__(self, Taxi.taxi_capacity, speed, position, None)
        self.image = image.load('img/taxi.png')
        self.city = city

    def get_next_element(self):
        ends = []
        for edge in self.city.edges():
            if self.city[edge[0]][edge[1]]['val'].begin == self.position:
                ends.append(self.city[edge[0]][edge[1]])
        return ends[randint(0, len(ends)-1)]

    def is_instance(self, transporter):
        return isinstance(transporter, Taxi)