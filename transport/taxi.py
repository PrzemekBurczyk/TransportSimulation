from pygame import image
from transport.transporter import Transporter
from random import randint
import networkx as nx

class Taxi(Transporter):
    taxi_capacity = 4
    taxi_speed = 10

    def __init__(self, position, city, speed=None):
        Transporter.__init__(self, Taxi.taxi_capacity, speed, position, None)
        self.image = image.load('img/taxi.png')
        self.city = city
        self.destination = self.set_destination()

    def get_next_element(self):
        path = nx.shortest_path(self.city, self.position, self.destination)
        return self.city[path[0]][path[1]]

    def is_instance(self, transporter):
        return isinstance(transporter, Taxi)

    def set_destination(self):
        points = []
        for edge in self.city.edges():
            if not points.__contains__(self.city[edge[0]][edge[1]]['val'].end):
                points.append(self.city[edge[0]][edge[1]]['val'].end)
        tmp_dest = points[randint(0, len(points)-1)]
        while tmp_dest == self.position:
            tmp_dest = points[randint(0, len(points)-1)]
        return tmp_dest

    def check_if_at_destination(self):
        return self.position == self.destination