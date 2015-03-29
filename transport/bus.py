from pygame import image
from transport.transporter import Transporter


class Bus(Transporter):
    bus_capacity = 40
    bus_speed = 5

    def __init__(self, env):
        Transporter.__init__(self, env, Bus.bus_capacity, Bus.bus_speed)
        self.image = image.load('img/bus.png')

    def run(self):
        while True:
            print('Bus running at %d' % self.env.now)
            yield self.env.timeout(self.speed)