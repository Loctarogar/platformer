# Platform game
import pygame
import random
from settings import *

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
    
    # game loop events
    def events(self):
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    
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