from random import randint
from pygame.sprite import Sprite


class Transporter(Sprite):
    max_capacity = 100
    max_speed = 10

    def __init__(self, capacity, speed, position, route):
        Sprite.__init__(self)
        if capacity is None:
            capacity = randint(1, Transporter.max_capacity)
        if speed is None:
            speed = randint(1, Transporter.max_speed)
        self.capacity = capacity
        self.speed = speed * 10
        self.lastTick = 0
        self.progress = 0.0
        self.route = route
        self.position = position

    def get_next_element(self):
        for edge in self.route.edges():
            if edge[0] == self.position:
                return edge
        return None
