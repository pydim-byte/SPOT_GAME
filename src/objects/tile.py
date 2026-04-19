import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,img):
        super().__init__()
        self.type = 'tile'
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,dt):
        pass

    def draw(self,surf,alpha):
        surf.blit(self.image,self.rect)