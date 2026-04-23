import pygame


class Xmark(pygame.sprite.Sprite):
    def __init__(self,pos,images,difference_number):
        super().__init__()
        self.type = 'xmark'
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = pos)

        self.difference_number = difference_number
        self.found = False

    def update(self,dt):
        pass

    def draw(self,surf,alpha):
        if not self.found:
            return
        surf.blit(self.image,self.rect)