import pygame
from ..globals import *


class Skull(pygame.sprite.Sprite):
    def __init__(self,pos,images):
        super().__init__()
        self.type = 'skull'
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = pos)

        self.hp = 2

        self.animation_max_time = 1.0
        self.animation_current_time = 0
        self.current_animation_frame = 0

    def animate(self,dt):
        if self.hp <= 0:
            return
        if self.animation_current_time >= self.animation_max_time:
            self.animation_current_time = 0
            self.current_animation_frame = (self.current_animation_frame + 1)%(len(self.images)-1)
            self.image = self.images[self.current_animation_frame]
        self.animation_current_time += dt
        

    def update(self,dt):
        self.animate(dt)

    def draw(self,surf,alpha):
        surf.blit(self.image,self.rect)


    