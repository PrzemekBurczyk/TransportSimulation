from pygame import image
from transport.transporter import Transporter


class Tram(Transporter):
    tram_capacity = 100
    tram_speed = 7

    def __init__(self, position=None, route=None, speed=None):
        Transporter.__init__(self, Tram.tram_capacity, speed, position, route)
        self.image = image.load('img/tram.png')