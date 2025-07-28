import pygame

class Ball:
    def __init__(self, x, y, speed_x, speed_y):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce_y(self):
        self.speed_y *= -1

    def check_wall_collision(self, width, height):
        if self.rect.left <= 0 or self.rect.right >= width:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 0, 0), self.rect)
