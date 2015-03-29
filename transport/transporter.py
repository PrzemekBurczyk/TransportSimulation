from random import randint
from pygame.sprite import Sprite


class Transporter(Sprite):
    max_capacity = 100
    max_speed = 10

    def __init__(self, env, capacity, speed):
        Sprite.__init__(self)
        if capacity is None:
            capacity = randint(1, Transporter.max_capacity)
        if speed is None:
            speed = randint(1, Transporter.max_speed)
        self.env = env
        self.capacity = capacity
        self.speed = speed
        # self.action = env.process(self.run())

    def run(self):
        while True:
            print('Running at %d' % self.env.now)