from pygame import image
from pygame.sprite import Sprite
from transport.taxi import Taxi

class Point():
    def __init__(self, x=0.0, y=0.0, point_types=None, load=0):
        # Sprite.__init__(self)
        if not point_types:
            point_types = ['none']
        self.x = x
        self.y = y
        self.point_types = point_types
        self.load = load
        self.available_load = load
        self.transporters = []
        self.image = image.load('img/point.png')
        # self.rect = self.image.get_rect(center=(self.x, self.y))

    def add_transporter(self, transporter):
        if transporter not in self.transporters:
            self.transporters.append(transporter)

    def may_transporter_go(self, transporter):
        if isinstance(transporter, Taxi):
            return True
        for t in self.transporters:
            if t.is_instance(transporter):
                return False
        return True