from pygame.sprite import Sprite


class RealSprite(Sprite):
    def __init__(self, sprite, real_width, real_height):
        Sprite.__init__(self)
        self.image = sprite.image
        self.rect = sprite.image.get_rect(center=(sprite.x * real_width, sprite.y * real_height))
