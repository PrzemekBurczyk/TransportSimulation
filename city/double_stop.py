from pygame import image
from city.bus_stop import BusStop
from city.tram_stop import TramStop


class DoubleStop(BusStop, TramStop):
    def __init__(self, x=0.0, y=0.0, point_types=None, load=0):
        if not point_types:
            point_types = ['bus', 'tram']
        BusStop.__init__(self, x, y, point_types, load)
        TramStop.__init__(self, x, y, point_types, load)
        self.image = image.load('img/double_stop.png')
