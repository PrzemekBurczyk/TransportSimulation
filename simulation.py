# coding=utf-8
import pygame
from pygame.sprite import Group
from environment import Environment
from real_sprite import RealSprite


class Simulation:

    def __init__(self, environment):
        self.environment = environment
        self.bus = self.environment.transporters[0]
        self.running = True
        self.screen = None
        self.size = self.width, self.height = 800, 600

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self, ticks):
        bus = self.environment.transporters[0]
        taxi = self.environment.transporters[1]
        tram = self.environment.transporters[2]
        bus2 = self.environment.transporters[3]
        bus.x = 0 + ticks / 100
        bus.y = 0 + ticks / 100
        bus.rect = bus.image.get_rect(center=(bus.x, bus.y))
        taxi.x = 800
        taxi.y = 600
        taxi.rect = taxi.image.get_rect(center=(taxi.x, taxi.y))
        tram.x = 800
        tram.y = 0
        tram.rect = tram.image.get_rect(center=(tram.x, tram.y))
        bus2.x = 0
        bus2.y = 600
        bus2.rect = bus2.image.get_rect(center=(bus2.x, bus2.y))

    def render_city(self, ticks):
        Group(map(lambda sprite: RealSprite(sprite, self.width, self.height), self.environment.city.nodes())).draw(self.screen)
        # self.environment.city.edges()

    def render_transporters(self, ticks):
        Group(self.environment.transporters).draw(self.screen)

    def on_render(self, ticks):
        self.screen.fill((255, 255, 255))

        self.render_city(ticks)
        self.render_transporters(ticks)

        # pygame.display.update()
        # – This updates the whole window (or the whole screen for fullscreen displays)

        # pygame.display.flip()
        # – This does the same thing,
        # and will also do the right thing if you’re using doublebuffered hardware acceleration

        # pygame.display.update(a rectangle or some list of rectangles)
        # – This updates just the rectangular areas of the screen you specify.

        # pygame.display.update()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)

            clock = pygame.time.Clock()
            ticks = pygame.time.get_ticks()

            self.on_loop(ticks)
            self.on_render(ticks)
        self.on_cleanup()


if __name__ == '__main__':
    simulation = Simulation(Environment())
    simulation.on_execute()
