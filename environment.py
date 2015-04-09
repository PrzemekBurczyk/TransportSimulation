from city.point import Point
from transport.bus import Bus
from transport.taxi import Taxi
from transport.tram import Tram
import networkx as nx


class Environment():

    points = []
    paths = []
    cycles = []
    speed = []

    for line in open('config/points'):
        p = line.strip().split(" ")
        if float(p[0]) < 0 or float(p[0]) > 1 or float(p[1]) < 0 or float(p[1]) > 1:
            exit("bad configuration: points coordinates must be between 0 and 1")
        points.append(Point(float(p[0]), float(p[1])))

    for line in open('config/paths'):
        p = line.strip().split(" ")
        path = []
        for point in p:
            path.append(int(point))
            if int(point) < 0 or int(point) > len(points):
                exit("bad configuration: point number mus be between 0 and " + str(len(points)))
        paths.append(path)

    for line in open('config/roads'):
        trans = line.strip().split(",")
        speed.append(int(trans[1]))
        r = trans[0].split(" ")
        road = []
        for point in r:
            road.append(int(point))
        cycles.append(road)

    def __init__(self):
        self.city = nx.DiGraph()
        self.transporters = []

        self.init_city()
        self.init_transporters()

    def init_transporters(self):
        for j in range(len(Environment.cycles)):
            cycle = Environment.cycles[j]
            road = nx.DiGraph()
            cycle_array = []
            for point in cycle:
                cycle_array.append(Environment.points[point])
            for i in range(len(cycle_array)):
                is_edge = False
                for edge in self.city.edges():
                    if (edge[0] == cycle_array[i] and edge[1] == cycle_array[(i+1)%len(cycle_array)]) or (edge[1] == cycle_array[i] and edge[0] == cycle_array[(i+1)%len(cycle_array)]):
                        is_edge = True
                if not is_edge:
                    exit("bad configuration: no connection between " + str(cycle_array[i].x) + "," + str(cycle_array[i].y) + " and " + str(cycle_array[(i+1)%len(cycle_array)].x) + "," + str(cycle_array[(i+1)%len(cycle_array)].y))
            road.add_cycle(cycle_array)
            self.transporters.append(Bus(Environment.points[cycle[0]], road, Environment.speed[j]))

    def init_city(self):
        for path in Environment.paths:
            path_array = []
            for point in path:
                path_array.append(Environment.points[point])
            self.city.add_path(path_array)