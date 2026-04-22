import pygame, sys
from src.globals import *
from src.tilemap import Tilemap
from src.player_controller import PlayerController
from src.physic_manager import PhysicManager


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.display = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()
        self.tilemap = Tilemap()
        self.player_controller = PlayerController(self.tilemap.player.sprite)
        self.physic_manager = PhysicManager(self.tilemap)

    def handle_inputs(self,inputs):
        self.player_controller.handle_inputs(inputs)

    def fixed_update(self):
        self.tilemap.player.sprite.fixed_update()
        self.physic_manager.fixed_update()

    def update(self,dt):
        self.tilemap.all_sprites.update(dt)

    def draw(self,alpha):
        self.tilemap.all_sprites.draw(self.screen,alpha)
        self.display.blit(pygame.transform.scale(self.screen,self.display.get_size()),(0,0))
        pygame.display.flip()

    def run(self):
        accumulator = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick(FPS) / 1000
            dt = min(dt,0.1)

            accumulator += dt

            while accumulator >= dt:
                self.handle_inputs(pygame.key.get_pressed())
                self.fixed_update()
                accumulator -= dt

            alpha = accumulator / dt

            self.update(dt)
            self.draw(alpha)

game = Game()
game.run()