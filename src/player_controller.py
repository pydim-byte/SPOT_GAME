import pygame


class PlayerController:
    def __init__(self,player):
        self.player = player

    def handle_inputs(self,inputs):
        move_direction = pygame.Vector2(0,0)
        if inputs['left']:
            move_direction.x = -1
        if inputs['right']:
            move_direction.x = 1
        if inputs['up']:
            move_direction.y = -1
        if inputs['down']:
            move_direction.y = 1
        self.player.set_direction(move_direction)
        
        if inputs['space']:
            self.player.guess()