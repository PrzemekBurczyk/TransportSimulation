from pygame import image
from transport.transporter import Transporter


class Bus(Transporter):
    bus_capacity = 40
    bus_speed = 5

    def __init__(self, position, route):
        Transporter.__init__(self, Bus.bus_capacity, Bus.bus_speed, position, route)
        self.image = image.load('img/bus.png')