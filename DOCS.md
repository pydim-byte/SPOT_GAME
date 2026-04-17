# TILEMAP

[ClearCode Turorial](https://github.com/clear-code-projects/Tiled/blob/main/code/tiled_code.py)

### Tile class

```
class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,img):
		super().__init__()
		self.image = img
		self.rect = self.image.get_rect(topleft = pos)

    def update(self,dt):
        pass

    def draw(self,surf,alpha):
        surf.blit(self.image,self.rect)
```

### Loading tiles

```
for layer in self.tmx_data.visible_layers:
	if hasattr(layer,'data'):
		for x,y,img in layer.tiles():
			pos = pygame.Vector2(x * TILE_SIZE * TILE_SCALE, y * TILE_SIZE * TILE_SCALE)
			Tile(pos,img)
```

### Loading objects

```
for obj in self.tmx_data.objects:
	pos = pygame.Vector2(obj.x,obj.y)
    images = self.get_images(
        obj.properties['obj_type'],
        obj.properties['images_variation']
        )
    if obj.properties['obj_type'] == 'player'"
	    self.player.add(Player(pos,images))
```

### Full Tilemap class

```
class Tilemap:
    pass
```

# Fixed timestep

[Gaffer tutorial](https://gafferongames.com/post/fix_your_timestep/)

### Before main loop

```
# Objects need to have pos and prev.pos
# General game shoul have FPS and FIXED_TPS
```

### In main loop

```
while True:
    dt = self.clock.tick(FPS) / 1000
    dt = min(dt,0.1)

    accumulator += dt

    while accumulator >= dt:
        self.fixed_update()
        self.handle_inputs(pygame.key.get_pressed())
        accumulator -= dt

    alpha = accumulator / dt

    self.update(dt)
    self.draw(alpha)
```

### Rendering with alpha

```



```