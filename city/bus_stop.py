from pygame import image
from city.point import Point


class BusStop(Point):
    def __init__(self, x=0.0, y=0.0, point_type='none', load=0):
        Point.__init__(self, x, y, point_type, load)
        self.image = image.load('img/bus_stop.png')
