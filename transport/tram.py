from pygame import image
from transport.transporter import Transporter


class Tram(Transporter):
    tram_capacity = 100
    tram_speed = 7

    def __init__(self, position):
        Transporter.__init__(self, Tram.tram_capacity, Tram.tram_speed, position)
        self.image = image.load('img/tram.png')