from shot import *
import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        if self.cooldown > 0:
            self.cooldown -= dt
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(0-dt)    
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown <= 0:
                self.shoot(pygame.Vector2(0,1).rotate(self.rotation))
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self, velocity):
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        bullet.velocity = velocity * PLAYER_SHOOT_SPEED
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        