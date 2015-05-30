from random import randint
from pygame.sprite import Sprite
import uuid

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
        self.speed = speed
        self.lastTick = 0
        self.progress = 0.0
        self.route = route
        self.position = position
        self.load = 0
        self.state = None
        self.id = uuid.uuid4()
        self.start_wait_ticks = None

    def get_capacity_left(self):
        return self.capacity - self.load

    def get_next_element(self):
        # print "position: " + str(self.position)
        for edge in self.route.edges():
            if self.route[edge[0]][edge[1]]['val'].begin == self.position:
                # print "chosen: " + str(self.route[edge[0]][edge[1]])
                return self.route[edge[0]][edge[1]]
        return None

    def is_instance(self, transporter):
        return False

    def start_waiting(self, ticks):
        self.start_wait_ticks = ticks

    def end_waiting(self, ticks):
        print(ticks - self.start_wait_ticks)
        self.start_wait_ticks = None