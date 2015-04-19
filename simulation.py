# coding=utf-8
import pygame
from pygame.sprite import Group
from city.point import Point
from environment import Environment
from real_sprite import RealSprite
import math


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
        for t in self.environment.transporters:
            if isinstance(t.position, Point):
                t.x = t.position.x * self.width
                t.y = t.position.y * self.height
                if t.lastTick + 1000 < ticks:
                    t.position = t.get_next_element()
                    t.progress = 0.0
                    t.lastTick = ticks
            else:
                position_val = t.position['val']
                speed = min([int(t.speed), int(position_val.max_speed)])*5
                t.progress += (ticks - t.lastTick) / 500000.0 * speed / math.sqrt((position_val.end.x - position_val.begin.x) * (position_val.end.x - position_val.begin.x) + (position_val.end.y - position_val.begin.y) * (position_val.end.y - position_val.begin.y))
                t.x = (position_val.begin.x + (position_val.end.x - position_val.begin.x) * t.progress) * self.width
                t.y = (position_val.begin.y + (position_val.end.y - position_val.begin.y) * t.progress) * self.height
                t.lastTick = ticks
                if t.progress >= 1.0:
                    t.position = position_val.end

            t.rect = t.image.get_rect(center=(t.x, t.y))

    def render_city(self, ticks):
        Group(map(lambda sprite: RealSprite(sprite, self.width, self.height), self.environment.city.nodes())).draw(self.screen)
        for edge in self.environment.city.edges():
            pygame.draw.aaline(self.screen, (0, 0, 0), (edge[0].x*self.width, edge[0].y*self.height), (edge[1].x*self.width, edge[1].y*self.height))

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
