import pygame
import math

from settings import Settings_dungeon_slach_game
from player import Player
from enemys import Enemy_A, Enemy_B, generate_enemy
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
            kwargs_input = {'dt': self.dt, 'x': 0, 'y': self.player.move_speed}
            for enemy in self.enemy_list:
                enemy.move(**kwargs_input)
            for bullet in self.bullets_list:
                bullet.move(**kwargs_input)
        
        
        if keys[pygame.K_s]:
            kwargs_input = {'dt': self.dt, 'x': 0, 'y': -self.player.move_speed}
            for enemy in self.enemy_list:
                enemy.move(**kwargs_input)
            for bullet in self.bullets_list:
                bullet.move(**kwargs_input)
        
        
        if keys[pygame.K_a]:
            kwargs_input = {'dt': self.dt, 'x': self.player.move_speed, 'y': 0}
            for enemy in self.enemy_list:
                enemy.move(**kwargs_input)
            for bullet in self.bullets_list:
                bullet.move(**kwargs_input)
        
        
        if keys[pygame.K_d]:
            kwargs_input = {'dt': self.dt, 'x': -self.player.move_speed, 'y': 0}
            for enemy in self.enemy_list:
                enemy.move(**kwargs_input)
            for bullet in self.bullets_list:
                bullet.move(**kwargs_input)
                


    def update(self):
        # dt = delt time
        # DPS locked on fixed value
        # use t value for independent physics
        self.dt = self.clock.tick(settings.DPS) / 1000
        
        # get mouse position
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        self.mouse_pos = [mouse_pos_x, mouse_pos_y - settings.score_surface_height]
        
        
        # player update
        self.player.update()
        
        
        # enemy update
        # check enemys cooldown and append new one
        if self.enemy_spawn_timer < self.enemy_spawn_cooldown:
            self.enemy_spawn_timer += self.dt
        else:
            self.enemy_list.append(generate_enemy(self.player.level))
            # reset enemy timer
            self.enemy_spawn_timer = 0
        # enemy movement
        for enemy in self.enemy_list:
            enemy.update(position = self.player.get_position_int())
            enemy.walk(self.dt)
        
        
        # bullets update
        # fire_rate check
        if self.fire_rate_timer < self.fire_rate:
            self.fire_rate_timer += self.dt
        else:
            angle = self.player.get_angle(self.mouse_pos)
            
            pos = self.player.get_position_int()
            self.bullets_list.append(Bullet(
                x = pos[0],
                y = pos[1],
                move_speed = self.player.bullet_move_speed,
                aoe = self.player.bullet_aoe,
                dmg = self.player.bullet_dmg,
                angle = angle,
                ))
            # reset enemy timer
            self.fire_rate_timer = 0
        # looping all bullets in the list
        for bullet_id, bullet in enumerate(self.bullets_list):
            # bullet movement
            bullet.walk(self.dt)
            # loop throu all enemys
            for enemy_id, enemy in enumerate(self.enemy_list):
                if bullet.get_distance(enemy.get_position_int()) < bullet.width:
                    # enemy hitted by bullet
                    bullet.detonate(pygame.time.get_ticks())
                    enemy.get_dmg(bullet.dmg)
                # enemy is killed
                if not enemy.alive:
                    self.player.exp += enemy.exp_value
                    self.enemy_list.pop(enemy_id)
                    self.player.score += 1
            
            # remove bullet if is too far
            if bullet.get_distance(self.player.get_position_int()) > self.player.fire_range:
                self.bullets_list.pop(bullet_id)
            
            
            # check alive of the bullet and destory it
            if bullet.alive:
                bullet.update(pygame.time.get_ticks())
            else:
                self.bullets_list.pop(bullet_id)
                
        
        
        
        # update score text
        self.score_text = f'Score = {self.player.score}'
        self.player_level_text = f'Level = {self.player.level}'
        self.player_hp_text = f'HP = {self.player.hp}'
        self.player_exp_text = f'EXP = {self.player.exp}'
        
        
    def draw(self):
        # fill screen in black
        self.screen.fill("black")
        
        
        # score surface
        self.score_surface.fill((170, 170, 170))
        # render score
        self.score_text_surface = self.score_font.render(self.score_text, True, (0, 0, 0))
        self.score_surface.blit(self.score_text_surface, (settings.score_surface_text_margin, settings.score_surface_text_margin))
        # render Player LEVEL
        self.player_level_text_surface = self.score_font.render(self.player_level_text, True, (0, 0, 0))
        self.score_surface.blit(self.player_level_text_surface, (settings.player_level_surface_text_margin_x, settings.score_surface_text_margin))
        # render Player HP
        self.player_hp_text_surface = self.score_font.render(self.player_hp_text, True, (0, 0, 0))
        self.score_surface.blit(self.player_hp_text_surface, (settings.player_hp_surface_text_margin_x, settings.score_surface_text_margin))
        # render Player EXP
        self.player_exp_text_surface = self.score_font.render(self.player_exp_text, True, (0, 0, 0))
        self.score_surface.blit(self.player_exp_text_surface, (settings.player_exp_surface_text_margin_x, settings.score_surface_text_margin))
        # exp_rect = pygame.Rect(left = 0, top = 90, width = 500, height = 8)
        # # exp_rect = pygame.Rect(left = 0,
        # #                        top = settings.score_surface_height - settings.player_exp_bar_height,
        # #                        width = settings.WIDTH * self.player.exp // self.player.to_next_level_difference,
        # #                        height = settings.player_exp_bar_height)
        # pygame.draw.rect(self.score_surface, (255, 100, 100), exp_rect)
        
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
    
    
    # def get_distance(pos1, pos2):
    #     return math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2 )
    
    
    # def get_angle(pos1, pos2):
    #     return math.atan2(pos2[1] - pos1[1], pos2[0] - pos1[0])

        