import pygame
from ..globals import *


class Skull(pygame.sprite.Sprite):
    def __init__(self,pos,images):
        super().__init__()
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = pos)


    def update(self,dt):
        pass

    def draw(self,surf,alpha):
        surf.blit(self.image,self.rect)


    