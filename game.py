import pygame
import math

from settings import Settings_dungeon_slach_game
from player import Player
from enemys import Enemy_A
from bullets import Bullet


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
        
        # create a Player on the middle of the screen
        self.player = Player(self.main_surface.get_width() // 2, self.main_surface.get_height() // 2)
        
        # create bullets list
        self.bullets_list = []
        self.fire_rate = self.player.fire_rate # value in seconds
        self.fire_rate_timer = 0
        
        # create list of the enemys
        self.enemy_list = []
        self.enemy_spawn_timer = 0
        self.enemy_spawn_cooldown = 0.5 # value in seconds
        
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
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            for enemy in self.enemy_list:
                enemy.move(dt = self.dt, x = 0, y = self.player.move_speed)
        if keys[pygame.K_s]:
            for enemy in self.enemy_list:
                enemy.move(dt = self.dt, x = 0, y = -self.player.move_speed)
        if keys[pygame.K_a]:
            for enemy in self.enemy_list:
                enemy.move(dt = self.dt, x = self.player.move_speed, y = 0)
        if keys[pygame.K_d]:
            for enemy in self.enemy_list:
                enemy.move(dt = self.dt, x = -self.player.move_speed, y = 0)


    def update(self):
        # dt = delt time
        # DPS locked on fixed value
        # use t value for independent physics
        self.dt = self.clock.tick(settings.DPS) / 1000
        
        # check enemys cooldown and append new one
        if self.enemy_spawn_timer < self.enemy_spawn_cooldown:
            self.enemy_spawn_timer += self.dt
        else:
            self.enemy_list.append(Enemy_A())
            # reset enemy timer
            self.enemy_spawn_timer = 0
        # enemy movement
        for enemy in self.enemy_list:
            enemy.update(player_x = self.player.x, player_y = self.player.y)
            enemy.walk(self.dt)
        
        
        # bullets update
        if self.fire_rate_timer < self.fire_rate:
            self.fire_rate_timer += self.dt
        else:
            angle = 1
            self.bullets_list.append(Bullet(
                x = self.player.x,
                y = self.player.y,
                move_speed = self.player.bullet_move_speed,
                angle = angle,
                ))
            # reset enemy timer
            self.fire_rate_timer = 0
        
        # bullet movement
        for bullet in self.bullets_list:
            bullet.update(player_x = self.player.x, player_y = self.player.y)
            bullet.walk(self.dt)
        
        
        
        # update score text
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
        # draw bullets
        for bullet in self.bullets_list:
            bullet.draw(self.main_surface)
        # draw enemys
        for enemy in self.enemy_list:
            enemy.draw(self.main_surface)
        

        # Blit the surfaces onto the main screen
        self.screen.blit(self.score_surface, (0, 0))
        self.screen.blit(self.main_surface, (0, settings.score_surface_height))
        
        # flip all game screen and surfaces
        pygame.display.flip()