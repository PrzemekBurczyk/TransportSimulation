from pygame import image
from pygame.sprite import Sprite


class Point():
    def __init__(self, x=0.0, y=0.0, point_types=None, load=0):
        # Sprite.__init__(self)
        if not point_types:
            point_types = ['none']
        self.x = x
        self.y = y
        self.point_types = point_types
        self.load = load
        self.transporter = None
        self.image = image.load('img/point.png')
        # self.rect = self.image.get_rect(center=(self.x, self.y))