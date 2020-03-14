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
        p1 = Platform(0, HEIGHT - 40, WIDTH, 40)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        p2 = Platform(WIDTH / 2 - 50, HEIGHT * 3/4, 100, 20)
        self.all_sprites.add(p2)
        self.platforms.add(p2)
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
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.rect.midbottom = self.player.pos
            self.player.vel.y = 0
    
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