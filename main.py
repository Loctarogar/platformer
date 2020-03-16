# Platform game
import pygame
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        self.running = True
        # initialize pygame and create window
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
    
    # start/reset game
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        # send to player reference to Game object
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for platform in PLATFORM_LIST:
            # *platform - explode list
            p = Platform(*platform)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()
    
    # game loop
    def run(self):
        self.clock.tick(FPS)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    # game loop update
    def update(self):
        # Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:            
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.rect.midbottom = self.player.pos
                self.player.vel.y = 0
        # if player reaches 1/4 of the screen
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for platform in self.platforms:
                platform.rect.y += abs(self.player.vel.y)
                
    
    # game loop events
    def events(self):
        # Process input (events)
        for event in pygame.event.get():
            # check for event
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
    
    # game loop - draw
    def draw(self):
        # Draw / render
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()
    
    def show_start_screen(self):
        pass
    
    def show_game_over_screen(self):
        pass

g = Game()

while g.running:
    g.new()
    g.show_game_over_screen()
    
pygame.quit()