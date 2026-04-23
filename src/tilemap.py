import pygame,random
from pytmx import load_pygame
from .globals import *
from .objects.tile import Tile
from .objects.player import Player
from .objects.skull import Skull
from .objects.barrier import Barrier
from .objects.heart import Heart
from .objects.skull_eye import Skull_eye
from .objects.xmark import Xmark
from .objects.difference import Difference
from .objects.particle import Particle


class Tilemap:
    def __init__(self,level_num=1):
        self.tmx_data = load_pygame(f'assets/tilemap/level_{level_num}.tmx')
        self.all_sprites = pygame.sprite.Group()
        self.visible_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.skull = pygame.sprite.GroupSingle()
        self.hearts = pygame.sprite.Group()
        self.skull_eyes = pygame.sprite.Group()
        self.xmarks = pygame.sprite.Group()
        self.particles = pygame.sprite.Group()
        self.barriers = []
        self.differences = []
        self.static_objects = []
        self.dynamic_objects = []
        self.get_tiles()

    def player_guess(self):
        guessed_right = False
        for d in self.differences:
            if self.player.sprite.rect.colliderect(d.rect):
                guessed_right = True
                for x in self.xmarks:
                    if x.difference_number == d.difference_number:
                        if x.found == True:
                            continue
                        self.skull.sprite.hp -= 1
                        x.found = True
                        SOUND_LIBRARY['right_guess'].play()
                        self.spawn_particles()
                for s in self.skull_eyes:
                    if s.skull_eye_number == d.difference_number:
                        s.damaged = True
        if not guessed_right:
            self.player.sprite.hp -= 1
            for h in self.hearts:
                if h.heart_number == (3 - self.player.sprite.hp):
                    h.damaged = True
                    SOUND_LIBRARY['wrong_guess'].play()
                    return

    def spawn_particles(self):
        for _ in range(100):
            pos = pygame.math.Vector2(self.player.sprite.rect.centerx,self.player.sprite.rect.centery)
            color = random.choice(('black','white'))
            direction = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
            direction = direction.normalize()
            speed = random.randint(4, 40)
            self.particles.add(Particle(pos, color, direction, speed))
        self.all_sprites.add(self.particles)
        self.dynamic_objects.extend(self.particles)

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
                self.player.add(Player(pos,images,self.player_guess))
            if obj.properties['obj_type'] == 'skull':
                self.skull.add(Skull(pos,images))
            if obj.properties['obj_type'] == 'barrier':
                self.barriers.append(Barrier(obj.x,obj.y,obj.width,obj.height))
            if obj.properties['obj_type'] == 'heart':
                self.hearts.add(Heart(pos,images,obj.properties['heart_number']))
            if obj.properties['obj_type'] == 'skull_eye':
                self.skull_eyes.add(Skull_eye(pos,images,obj.properties['skull_eye_number']))
            if obj.properties['obj_type'] == 'xmark':
                self.xmarks.add(Xmark(pos,images,obj.properties['difference_number']))
            if obj.properties['obj_type'] == 'difference':
                self.differences.append(Difference(obj.x,obj.y,obj.width,obj.height,obj.properties['difference_number']))

        self.all_sprites.add(self.visible_tiles)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.skull)
        self.all_sprites.add(self.hearts)
        self.all_sprites.add(self.skull_eyes)
        self.all_sprites.add(self.xmarks)

        self.static_objects.extend(self.barriers)
        self.dynamic_objects.append(self.player.sprite)

    def get_images(self,obj_type,image_count):
        images = []
        for img in range(image_count):
            images.append(pygame.image.load(f'assets/images/{obj_type}/{img}.png').convert_alpha())
        return images