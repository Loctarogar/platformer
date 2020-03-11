# Sprite classes for platform game
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        # positional vector
        self.pos = pygame.math.Vector2(WIDTH/2, HEIGHT/2)
        # velocity vector
        self.vel = pygame.math.Vector2(0, 0)
        # acceleration vector
        self.acc = pygame.math.Vector2(0, 0)
        
    def update(self):
        self.acc = pygame.math.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            
        self.acc += self.vel * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        self.rect.center = self.pos