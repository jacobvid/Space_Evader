import os
import pygame

from ship import Ship


class AlienShip(Ship):
    def __init__(self, x, y, image_filename):
        images_dir = "Images"  # Folder containing images
        cwd = os.path.dirname(__file__)  # Get the current directory of the script
        image_path = os.path.join(cwd, images_dir, image_filename)
        super().__init__(x, y, image_path)
        self.image = pygame.image.load(image_path).convert_alpha() if os.path.exists(image_path) else None
        self.speed = 50
        self.direction = 1

    def draw(self, window):
        if self.image:
            window.blit(self.image, (self.x, self.y))  # Draw alien ship image on the window

    def resize_image(self, width, height):
        if self.image:
            self.image = pygame.transform.scale(self.image, (width, height))

    def move(self, dt):
        self.x += self.direction * self.speed * dt

    def change_direction(self):
        self.direction *= -1

    def set_speed(self, speed):
        self.speed = speed
