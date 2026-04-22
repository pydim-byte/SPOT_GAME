import pygame


class Skull_eye(pygame.sprite.Sprite):
    def __init__(self,pos,images,skull_eye_number):
        super().__init__()
        self.type = 'skull_eye'
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = pos)

        self.skull_eye_number = skull_eye_number
        self.damaged = False

    def update(self,dt):
        pass

    def draw(self,surf,alpha):
        surf.blit(self.image,self.rect)