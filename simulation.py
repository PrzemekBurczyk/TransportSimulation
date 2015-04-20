# coding=utf-8
import pygame
from pygame.sprite import Group
from city.point import Point
from environment import Environment
from real_sprite import RealSprite
from random import randint
import math


class Simulation:

    COLORS = {
        'white': (255, 255, 255),
        'black': (0, 0, 0)
    }

    TICKS_PER_LOAD_CHANGE = 100

    def __init__(self, environment):
        self.environment = environment
        self.bus = self.environment.transporters[0]
        self.running = True
        self.screen = None
        self.size = self.width, self.height = 800, 600
        self.font_normal = None

    def on_init(self):
        pygame.init()
        self.font_normal = pygame.font.SysFont("monospace", 15)
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
                if t.state == 'driving' or t.state is None:
                    t.load_out = randint(0, t.load)
                    t.load_in = randint(0, min(t.position.load, t.get_capacity_left() + t.load_out))
                    t.state = 'loadingOut'
                    t.lastTick = ticks
                else:
                    load_change = int((ticks - t.lastTick) / Simulation.TICKS_PER_LOAD_CHANGE)
                    if load_change > 0:
                        if t.state == 'loadingIn':
                            t.load_in -= load_change
                            if t.load_in <= 0:
                                load_change += t.load_in
                                t.state = 'driving'
                            t.load += load_change
                            t.position.load -= load_change
                            if t.state == 'driving':
                                t.position = t.get_next_element()
                                t.progress = 0.0
                            t.lastTick = ticks
                        elif t.state == 'loadingOut':
                            t.load_out -= load_change
                            if t.load_out <= 0:
                                load_change += t.load_out
                                t.state = 'loadingIn'
                            t.load -= load_change
                            t.position.load += load_change
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

    def draw_text_real(self, text, real_x, real_y, color):
        if color is None:
            color = Simulation.COLORS['white']
        text = self.font_normal.render(str(text), True, color)
        text_position = text.get_rect(center=(real_x, real_y))
        self.screen.blit(text, text_position)

    def draw_text(self, text, x, y, color):
        self.draw_text_real(text, x * self.width, y * self.height, color)

    def render_city(self, ticks):

        # draw edges
        for edge in self.environment.city.edges():
            pygame.draw.aaline(self.screen, Simulation.COLORS['black'], (edge[0].x * self.width, edge[0].y * self.height), (edge[1].x * self.width, edge[1].y * self.height))

        # draw stops / points
        Group(map(lambda sprite: RealSprite(sprite, self.width, self.height), self.environment.city.nodes())).draw(self.screen)

        # draw labels / texts on top
        for node in self.environment.city.nodes():
            self.draw_text(node.load, node.x, node.y, Simulation.COLORS['white'])

    def render_transporters(self, ticks):

        # draw transporter sprites
        Group(self.environment.transporters).draw(self.screen)

        # draw transporter labels / texts on top
        for transporter in self.environment.transporters:
            self.draw_text_real(transporter.load, transporter.x, transporter.y, Simulation.COLORS['white'])

    def on_render(self, ticks):
        self.screen.fill(Simulation.COLORS['white'])

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
