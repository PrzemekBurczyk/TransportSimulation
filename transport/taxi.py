from pygame import image
from transport.transporter import Transporter


class Taxi(Transporter):
    taxi_capacity = 3
    taxi_speed = 10

    def __init__(self, position):
        Transporter.__init__(self, Taxi.taxi_capacity, Taxi.taxi_speed, position)
        self.image = image.load('img/taxi.png')

    def is_instance(self, transporter):
        return isinstance(transporter, Taxi)