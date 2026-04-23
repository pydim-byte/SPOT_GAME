import pygame


class Difference:
    def __init__(self,x,y,width,height,difference_number):
        self.type = 'barrier'
        self.rect = pygame.Rect(x,y,width,height)
        self.difference_number = difference_number
