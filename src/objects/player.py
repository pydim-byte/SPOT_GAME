import pygame
from ..globals import *


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,images):
        super().__init__()
        self.type = 'player'
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = pos)

        self.hp = 3

        self.pos = pos
        self.prev_pos = self.pos.copy()
        self.direction = pygame.Vector2(0,0)
        self.movement_direction = pygame.Vector2(0,0)
        self.vel = pygame.Vector2(0,0)

    def set_direction(self,direction):
        self.movement_direction.xy = direction.xy

    def calculate_velocity(self):
        self.direction.xy = self.movement_direction.xy
        self.vel.xy = self.direction.xy * PLAYER_MOVEMENT_SPEED

    def fixed_update(self):
        self.prev_pos.xy = self.pos.xy

    def update(self,dt):
        pass

    def draw(self,surf,alpha):
        alpha_pos = self.pos * alpha + self.prev_pos * (1 - alpha)
        draw_rect = self.rect.copy()
        draw_rect.topleft = alpha_pos

        surf.blit(self.image,draw_rect)


    