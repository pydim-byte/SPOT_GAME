import pygame


class PhysicManager:
    def __init__(self,obj_data):
        self.static_objects = obj_data.static_objects
        self.dynamic_objets = obj_data.dynamic_objects

    @property
    def physical_objects(self):
        return self.static_objects + self.dynamic_objets
    
    def move_horizontal(self,obj):
        obj.rect.x += obj.vel.x
        obj.pos.x = obj.rect.x

    def check_horizontal_collision(self,obj):
        if obj.type == 'particle':
            return
        
        for collision_obj in self.static_objects:
            if not collision_obj.alive():
                continue
            if not obj.rect.colliderect(collision_obj.rect):
                continue
            if obj.vel.x > 0:
                obj.rect.right = collision_obj.rect.left
            if obj.vel.x < 0:
                obj.rect.left = collision_obj.rect.right
        obj.vel.x = 0
        obj.pos.x = obj.rect.x

    def move_vertical(self,obj):
        obj.rect.y += obj.vel.y
        obj.pos.y = obj.rect.y

    def check_vertical_collision(self,obj):
        if obj.type == 'particle':
            return

        for collision_obj in self.static_objects:
            if not collision_obj.alive():
                continue
            if not obj.rect.colliderect(collision_obj.rect):
                continue
            if obj.vel.y > 0:
                obj.rect.bottom = collision_obj.rect.top
            if obj.vel.y < 0:
                obj.rect.top = collision_obj.rect.bottom
            obj.vel.y = 0
            obj.pos.y = obj.rect.y  

    def move_and_collide(self,obj):
        if not obj.alive():
            return

        obj.calculate_velocity()
        self.move_horizontal(obj)
        self.check_horizontal_collision(obj)
        self.move_vertical(obj)
        self.check_vertical_collision(obj)

    def fixed_update(self):
        for obj in self.dynamic_objets:
            self.move_and_collide(obj)