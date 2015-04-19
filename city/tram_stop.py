from pygame import image
from city.point import Point


class TramStop(Point):
    def __init__(self, x=0.0, y=0.0, point_types=None, load=0):
        if not point_types:
            point_types = ['tram']
        Point.__init__(self, x, y, point_types, load)
        self.image = image.load('img/tram_stop.png')
