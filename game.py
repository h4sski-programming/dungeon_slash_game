import pygame

from settings import Settings_dungeon_slach_game
from player import Player

settings = Settings_dungeon_slach_game()


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.resolution)
        pygame.display.set_caption(settings.title)
        
    
    def run(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        
        # initiate 2 Surfaces
        self.score_surface = pygame.Surface((settings.resolution[0], settings.score_surface_height))
        self.main_surface = pygame.Surface((settings.resolution[0], settings.resolution[1] - settings.score_surface_height))
        
        self.score_font = pygame.font.Font(None, settings.score_surface_text_font_size)
        
        # create Player on the middle of the screen
        self.player = Player(self.main_surface.get_width() // 2, self.main_surface.get_height() // 2)
        
        # main loop of the game
        while self.running:
            self.events()
            self.update()
            self.draw()
        
        pygame.quit()
            
            
    def events(self):
        # QUIT game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def update(self):
        # dt = delt time
        # DPS locked on fixed value
        # use t value for independent physics
        self.dt = self.clock.tick(settings.DPS) / 1000
        
        self.score_text = f'Score = {self.player.score}'
        
        
    def draw(self):
        # fill screen in black
        self.screen.fill("black")
        
        
        # score surface
        self.score_surface.fill((170, 170, 170))
        # render score
        self.score_text_surface = self.score_font.render(self.score_text, True, (0, 0, 0))
        self.score_surface.blit(self.score_text_surface, (settings.score_surface_text_margin, settings.score_surface_text_margin))
        
        
        # main surface
        self.main_surface.fill((0, 0, 0))
        # draw player at self.main_surface
        self.player.draw(self.main_surface)
        

        # Blit the surfaces onto the main screen
        self.screen.blit(self.score_surface, (0, 0))
        self.screen.blit(self.main_surface, (0, settings.score_surface_height))
        
        # flip all game screen and surfaces
        pygame.display.flip()