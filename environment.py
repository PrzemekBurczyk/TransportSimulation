from city.bus_stop import BusStop
from city.double_stop import DoubleStop
from city.point import Point
from city.tram_stop import TramStop
from transport.bus import Bus
from transport.taxi import Taxi
from transport.tram import Tram
import networkx as nx
from city.edge import Edge


class Environment():

    def __init__(self):
        self.points = []
        self.paths = []
        self.cycles = []
        self.speed = []
        self.edge_speed = []
        self.transporters = []

        self.load_points()
        self.load_paths()
        self.load_roads()

        self.city = nx.DiGraph()
        self.init_city()
        self.init_transporters()

    def load_points(self):
        for line in open('config/points'):
            if line.startswith("#"):
                continue
            p = line.strip().split(" ")
            x = float(p[0])
            y = float(p[1])
            point_types = p[2].split(",")
            load = int(p[3])
            if x < 0 or x > 1 or y < 0 or y > 1:
                exit("bad configuration: points coordinates must be between 0 and 1")
            if len(point_types) == 1:
                point_type = point_types[0]
                if point_type == 'bus':
                    self.points.append(BusStop(x, y, point_types, load))
                elif point_type == 'tram':
                    self.points.append(TramStop(x, y, point_types, load))
                elif point_type == 'none':
                    self.points.append(Point(x, y, point_types, load))
                else:
                    exit("bad configuration: point types must be one of: 'bus', 'tram', 'none'")
            else:
                if len(point_types) == 2 and 'bus' in point_types and 'tram' in point_types:
                    self.points.append(DoubleStop(x, y, point_types, load))
                else:
                    exit("bad configuration: unknown point types combination")

    def load_paths(self):
        for line in open('config/paths'):
            full_path = line.strip().split(",")
            self.edge_speed.append(full_path[1])
            p = full_path[0].split(" ")
            path = []
            for point in p:
                path.append(int(point))
                if int(point) < 0 or int(point) > len(self.points):
                    exit("bad configuration: point number must be between 0 and " + str(len(self.points)))
            self.paths.append(path)

    def load_roads(self):
        for line in open('config/roads'):
            trans = line.strip().split(",")
            self.speed.append(int(trans[1]))
            transporter_type = trans[2]
            if transporter_type == "bus":
                self.transporters.append(Bus())
            elif transporter_type == "tram":
                self.transporters.append(Tram())
            # elif transporter_type == "taxi":
                # self.transporters.append(Taxi())
            else:
                exit("bad configuration: transporter type must be one of: 'bus', 'tram', 'taxi'")
            r = trans[0].split(" ")
            road = []
            for point in r:
                road.append(int(point))
            self.cycles.append(road)

    def init_transporters(self):
        for j in range(len(self.cycles)):
            cycle = self.cycles[j]
            road = nx.DiGraph()
            cycle_array = []
            for point in cycle:
                cycle_array.append(self.points[point])
            for i in range(len(cycle_array)):
                is_edge = False
                for edge in self.city.edges():
                    edge_val = self.city[edge[0]][edge[1]]['val']
                    if (edge_val.begin == cycle_array[i] and edge_val.end == cycle_array[(i+1) % len(cycle_array)]) or (edge_val.end == cycle_array[i] and edge_val.begin == cycle_array[(i+1) % len(cycle_array)]):
                        is_edge = True
                        road.add_edge(edge[0], edge[1], val=edge_val)
                if not is_edge:
                    exit("bad configuration: no connection between " + str(cycle_array[i].x) + "," + str(cycle_array[i].y) + " and " + str(cycle_array[(i+1) % len(cycle_array)].x) + "," + str(cycle_array[(i+1) % len(cycle_array)].y))

            # road.add_cycle(cycle_array)
            self.transporters[j].position = self.points[cycle[0]]
            self.transporters[j].route = road
            self.transporters[j].speed = self.speed[j]
            # self.transporters.append(Bus(self.points[cycle[0]], road, self.speed[j]))

    def init_city(self):
        for i in range(len(self.paths)):
            path = self.paths[i]
            self.city.add_edge(self.points[path[0]], self.points[path[1]], val=Edge(self.points[path[0]], self.points[path[1]], self.edge_speed[i]))
