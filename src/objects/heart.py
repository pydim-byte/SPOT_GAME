import pygame


class Heart(pygame.sprite.Sprite):
    def __init__(self,pos,images,heart_number):
        super().__init__()
        self.type = 'health'
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = pos)

        self.heart_number = heart_number
        self.damaged = False

    def update(self,dt):
        pass

    def draw(self,surf,alpha):
        surf.blit(self.image,self.rect)