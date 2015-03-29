import simpy

from transport.bus import Bus
from transport.taxi import Taxi
from transport.tram import Tram


run_time = 1000000

env = simpy.Environment()
bus = Bus(env)
tram = Tram(env)
taxi = Taxi(env)


def run_simulation():
    env.run(until=run_time)



