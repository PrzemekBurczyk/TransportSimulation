from pygame import image
from transport.transporter import Transporter


class Tram(Transporter):
    tram_capacity = 100
    tram_speed = 7

    def __init__(self, env):
        Transporter.__init__(self, env, Tram.tram_capacity, Tram.tram_speed)
        self.image = image.load('img/tram.png')

    def run(self):
        while True:
            print('Tram running at %d' % self.env.now)
            yield self.env.timeout(self.speed)