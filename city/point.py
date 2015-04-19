from pygame import image
from pygame.sprite import Sprite


class Point():
    def __init__(self, x=0.0, y=0.0, point_type='none', load=0):
        # Sprite.__init__(self)
        self.x = x
        self.y = y
        self.point_type = point_type
        self.load = load
        self.image = image.load('img/point.png')
        # self.rect = self.image.get_rect(center=(self.x, self.y))