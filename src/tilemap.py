import pygame
from pytmx import load_pygame
from .globals import *
from .objects.tile import Tile
from .objects.player import Player
from .objects.skull import Skull
from .objects.barrier import Barrier
from .objects.heart import Heart
from .objects.skull_eye import Skull_eye


class Tilemap:
    def __init__(self,level_num=1):
        self.tmx_data = load_pygame(f'assets/tilemap/level_{level_num}.tmx')
        self.all_sprites = pygame.sprite.Group()
        self.visible_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.skull = pygame.sprite.GroupSingle()
        self.hearts = pygame.sprite.Group()
        self.skull_eyes = pygame.sprite.Group()
        self.barriers = []
        self.static_objects = []
        self.dynamic_objects = []
        self.get_tiles()

    def get_tiles(self):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer,'data'):
                for x,y,img in layer.tiles():
                    pos = pygame.Vector2(x * TILE_SIZE * TILE_SCALE, y * TILE_SIZE * TILE_SCALE)
                    self.visible_tiles.add(Tile(pos,img))

        for obj in self.tmx_data.objects:
            pos = pygame.Vector2(obj.x,obj.y)
            images = self.get_images(
                obj.properties['obj_type'],
                obj.properties['images_variation']
                )
            if obj.properties['obj_type'] == 'player':
                self.player.add(Player(pos,images))
            if obj.properties['obj_type'] == 'skull':
                self.skull.add(Skull(pos,images))
            if obj.properties['obj_type'] == 'barrier':
                self.barriers.append(Barrier(obj.x,obj.y,obj.width,obj.height))
            if obj.properties['obj_type'] == 'heart':
                self.hearts.add(Heart(pos,images,obj.properties['heart_number']))
            if obj.properties['obj_type'] == 'skull_eye':
                self.skull_eyes.add(Skull_eye(pos,images,obj.properties['skull_eye_number']))

        self.all_sprites.add(self.visible_tiles)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.skull)
        self.all_sprites.add(self.hearts)
        self.all_sprites.add(self.skull_eyes)

        self.static_objects.extend(self.barriers)
        self.dynamic_objects.append(self.player.sprite)



    def get_images(self,obj_type,image_count):
        images = []
        for img in range(image_count):
            images.append(pygame.image.load(f'assets/images/{obj_type}/{img}.png').convert_alpha())
        return images