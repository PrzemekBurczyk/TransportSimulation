from city.point import Point
from transport.bus import Bus
from transport.taxi import Taxi
from transport.tram import Tram
import networkx as nx


class Environment():

    point1 = Point(0.1, 0.1)
    point2 = Point(0.9, 0.1)
    point3 = Point(0.1, 0.9)
    point4 = Point(0.9, 0.9)
    point5 = Point(0.5, 0.5)

    def __init__(self):
        self.city = nx.DiGraph()
        self.transporters = []

        self.init_city()
        self.init_transporters()

    def init_transporters(self):
        self.transporters.append(Bus(Environment.point1, self.city.subgraph([Environment.point1, Environment.point5, Environment.point3])))

    def init_city(self):
        self.city.add_path([Environment.point2, Environment.point1, Environment.point5, Environment.point3, Environment.point4])
        self.city.add_path([Environment.point3, Environment.point1])