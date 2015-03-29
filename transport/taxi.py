from pygame import image
from transport.transporter import Transporter


class Taxi(Transporter):
    taxi_capacity = 3
    taxi_speed = 10

    def __init__(self, env):
        Transporter.__init__(self, env, Taxi.taxi_capacity, Taxi.taxi_speed)
        self.image = image.load('img/taxi.png')

    def run(self):
        while True:
            print('Taxi running at %d' % self.env.now)
            yield self.env.timeout(self.speed)