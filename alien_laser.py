import pygame


class AlienLaser:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 3  # Laser width
        self.height = 10  # Laser height
        self.color = (255, 0, 0)  # Red color for the laser

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def move(self, speed):
        self.y += speed  # Move the laser downwards based on the given speed
