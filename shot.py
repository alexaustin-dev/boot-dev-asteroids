from constants import SHOT_RADIUS
import pygame
import math
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt