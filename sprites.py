# Sprite classes for platform game
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        # positional vector
        self.pos = pygame.math.Vector2(WIDTH/2, HEIGHT/2)
        # velocity vector
        self.vel = pygame.math.Vector2(0, 0)
        # acceleration vector
        # pygame.math.Vector2(x_vector, y_vector)
        self.acc = pygame.math.Vector2(0, 0)

    def update(self):
        self.acc = pygame.math.Vector2(0, PLAYER_GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equation of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap arount the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        
        self.rect.midbottom = self.pos
        
    def jump(self):
        # jump only if standing on a platform
        # add + 1 pixel to check collision
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        # return player back
        self.rect.y -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
        
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        