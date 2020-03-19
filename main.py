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
        self.font_name = pygame.font.match_font(FONT_NAME)
    
    # start/reset game
    def new(self):
        self.score = 0
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
                if platform.rect.top >= HEIGHT:
                    platform.kill()
                    # add scores
                    self.score += 10
                    
        # spawn new platforms
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            platform = Platform(random.randrange(0, WIDTH-width),
                                random.randrange(-75, -30),
                                width, 20)
            self.platforms.add(platform)
            self.all_sprites.add(platform)
            
        # Die!
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

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
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 16)
        
        # *after* drawing everything, flip the display
        pygame.display.flip()

    def show_start_screen(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE,WIDTH/2, HEIGHT/4)
        self.draw_text("Arrows to move", 22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press a key", 22, WHITE, WIDTH/2, HEIGHT *3/4)
        pygame.display.flip()
        self.wait_for_key()

    def show_game_over_screen(self):
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text('Game Over', 48, WHITE,WIDTH/2, HEIGHT/4)
        self.draw_text("Score: " + str(self.score ), 22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press a key", 22, WHITE, WIDTH/2, HEIGHT *3/4)
        pygame.display.flip()
        self.wait_for_key()
    
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()

while g.running:
    g.show_start_screen()
    g.new()
    g.show_game_over_screen()
    
pygame.quit()