import pygame


class PlayerController:
    def __init__(self,player):
        self.player = player

    def handle_inputs(self,inputs):
        move_direction = pygame.Vector2(0,0)
        if inputs[pygame.K_LEFT]:
            move_direction.x = -1
        if inputs[pygame.K_RIGHT]:
            move_direction.x = 1
        if inputs[pygame.K_UP]:
            move_direction.y = -1
        if inputs[pygame.K_DOWN]:
            move_direction.y = 1
        self.player.set_direction(move_direction)
        