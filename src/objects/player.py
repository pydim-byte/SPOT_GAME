import pygame
from ..globals import *


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,images):
        super().__init__()
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = pos)
        self.pos = pos
        self.prev_pos = self.pos.copy()
        self.direction = pygame.Vector2(0,0)
        self.movement_direction = pygame.Vector2(0,0)
        self.speed = 2

    def set_direction(self,direction):
        self.movement_direction.xy = direction.xy

    def move_and_colide(self):
        self.prev_pos = self.pos.copy()
        self.direction.xy = self.movement_direction.xy
        self.rect.topleft += self.direction * self.speed
        self.rect.clamp_ip(pygame.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT))
        self.pos.xy = self.rect.topleft

    def fixed_update(self):
        self.move_and_colide()

    def update(self,dt):
        pass

    def draw(self,surf,alpha):
        alpha_pos = self.pos * alpha + self.prev_pos * (1 - alpha)
        draw_rect = self.rect.copy()
        draw_rect.topleft = alpha_pos

        surf.blit(self.image,draw_rect)


    