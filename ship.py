import pygame


class Ship:
    def __init__(self, x, y, image_filename):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def resize_image(self, width, height):
        if self.image:
            self.image = pygame.transform.scale(self.image, (width, height))

    def at_edge(self, width):
        return self.x <= 0 or self.x >= width - self.image.get_width()

    def move(self, dt):
        pass
