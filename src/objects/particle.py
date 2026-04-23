import pygame
from ..globals import *


class Particle(pygame.sprite.Sprite):
    def __init__(self,pos,color,direction,speed):
        super().__init__()
        self.type = 'particle'
        self.color = color
        self.size = 4

        self.image = pygame.Surface((self.size, self.size)).convert_alpha()
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect(topleft=pos)

        self.lifetime = 4

        self.pos = pos
        self.prev_pos = self.pos.copy()
        self.direction = direction
        self.speed = speed
        self.vel = pygame.Vector2(0,0)

    def calculate_velocity(self):
        self.vel = self.direction * self.speed

    def fixed_update(self):
        self.prev_pos.xy = self.pos.xy

    def kill_countdown(self,dt):
        if self.lifetime <= 0:
            self.kill()
        self.lifetime -= dt

    def update(self, dt):
        self.kill_countdown(dt)

    def draw(self,surf,alpha):
        alpha_pos = self.pos * alpha + self.prev_pos * (1 - alpha)
        draw_rect = self.rect.copy()
        draw_rect.topleft = alpha_pos

        pygame.draw.rect(surf,self.color,draw_rect)