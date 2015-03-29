from city.point import Point
from transport.bus import Bus
from transport.taxi import Taxi
from transport.tram import Tram
import networkx as nx


class Environment():
    def __init__(self):
        self.city = nx.Graph()
        self.transporters = []

        self.init_city()
        self.init_transporters()

    def init_transporters(self):
        self.transporters.append(Bus(None))
        self.transporters.append(Taxi(None))
        self.transporters.append(Tram(None))
        self.transporters.append(Bus(None))

    def init_city(self):
        self.city.add_node(Point(0.1, 0.1))
        self.city.add_node(Point(0.9, 0.1))
        self.city.add_node(Point(0.1, 0.9))
        self.city.add_node(Point(0.9, 0.9))
        self.city.add_node(Point(0.5, 0.5))
        self.city.add_edge(self.city.nodes()[0], self.city.nodes()[1])