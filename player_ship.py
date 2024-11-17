import os
import pygame

from ship import Ship


class PlayerShip(Ship):
    def __init__(self, x, y, image_filename):
        images_dir = "Images"  # Folder containing images
        cwd = os.path.dirname(__file__)  # Get the current directory of the script
        image_path = os.path.join(cwd, images_dir, image_filename)
        super().__init__(x, y, image_path)
        self.image = pygame.image.load(image_path).convert_alpha() if os.path.exists(image_path) else None

    def move_left(self, step=5):
        self.x -= step

    def move_right(self, step=5):
        self.x += step

    def update_position(self, keys, width):
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if self.x > width - 50:
            self.x = -50
        if self.x < -50:
            self.x = width - 50

    def draw(self, window):
        if self.image:
            window.blit(self.image, (self.x, self.y))  # Draw player ship image on the window

    def resize_image(self, width, height):
        if self.image:
            self.image = pygame.transform.scale(self.image, (width, height))
