# game/paddle.py
import pygame

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 120, 15)
        self.speed = 7

    def move(self, direction):
        self.rect.x += direction * self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800

    def reset(self, x):
        self.rect.x = x

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)
