#! /usr/bin/env python3
# coding: utf-8

"""
Game    : McGyver maze
File    : game.py
Creator : Grégory Le Terte
Info    : Initialization of pygame, management of menu or level window displays,
           here we manage the game
"""

import pygame as pg
import sys
import os
import time

sys.path.append("./")
from src.constants import *
from src.level import Level
from src.characters import Macgyver, Structure_map
from src.display import Display
from src.configjson import ConfigJson

class Game:

    def __init__(self, level, time_game):

        """ Start game Mac Gyver
            Args:
                level: if level=0 then we launch the game menu but if level>0
                        launch level
                time_game: we keep the time between the levels
        """
        self.playing = False
        self.level_number = 0
        self.time_game = time_game

        # We get the path of the map_x.txt file
        spath = Level(level)

        # Level structure
        self.structure_map = Structure_map(spath.path_file)
        self.level_number = spath.number_level

        # Init Pygame for screen
        self.initialize_pygame()

        # music game
        self.manage_sound()


    def initialize_pygame(self):
        """ Pygame initialization, screen and messages creation,
            classes calling
        """

        pg.init()
        pg.font.init()

        # Display window
        size_screen = int(SIZE_SPRITES * NB_SPRITES)
        self.screen = pg.display.set_mode((size_screen, size_screen))
        self.title = pg.display.set_caption(
            TITLE + "             LEVEL : " + str(self.level_number))
        self.icon = pg.image.load(ICON).convert_alpha()
        pg.display.set_icon(self.icon)

        # Message for user
        self.message = pg.font.SysFont(None, 30)
        self.win5 = self.message.render('You are a champion of MAZE', True,
                                        (255, 255, 255))
        self.lost = self.message.render('YOU LOST ! The guardian captured you',
                                        True, (255, 255, 255))

        # Instancie characters
        self.macgyver = Macgyver(self.structure_map)

        # Initialization time
        self.clock = pg.time.Clock()
        self.time_game_display = round(time.time() - self.time_game)

        # Instancie Display screen
        self.display = Display()

    def manage_sound(self):
        """ Manage music game """
        file_mp3 = f"Level_{str(self.level_number)}" + ".mp3"
        file_sound = str(os.getcwd() + "/resources/sound/" + file_mp3 )

        pg.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pg.mixer.music.load(file_sound)
        pg.mixer.music.play(0)

    def start(self):
        """ Method which runs the game, with the maps display, the keyboard
            controls and the victory conditions
        """

        # Initialization of variables
        self.playing = True

        # Loop game
        while self.playing:
            # Time
            self.time_game = round(time.time() - self.time_game_display)
            # Display sreen
            self.display.display_map(self.structure_map, self.screen)
            # Manege events keyboard
            self.keyboard_events()
            # Recovered objects
            self.items_counter()
            # Management of the end of the game
            self.endings()
            # Method should be called once per frame
            self.clock.tick(30)

    def endings(self):
        """ Method called if MacGyver is in front of the guard with or
            without all objects
        """

        # displaying a gain or loss and game end message.
        if self.structure_map.map_array[self.macgyver.y][self.macgyver.x + 1] == 'G':

            if self.macgyver.items_collected == 3:
                # Case if we recovered all 3 objects
                self.rect = pg.draw.rect(self.screen, (18, 99, 18), [0, 300, 600, 80])

                # If so, at what level are we?
                if self.level_number == 5:
                    # End of game - Winner, display Text and save file
                    self.display_message_winner()
            else:
                # End of game - Lost, display Text
                self.display_message_lost()

            # stop loop game : start()
            self.playing = False

    def display_message_winner(self):
        """ We calculate if the player was the fastest to do the 5 levels """
        self.screen.blit(self.win5, (155, 315))

        time = self.cutHour(self.time_game)
        time_valeur = str(time)
        time_valeur = time_valeur.replace(':', '')
        winenertime_valeur = str(WINNER_TIME)
        winenertime_valeur = winenertime_valeur.replace(':', '')

        if int(time_valeur) < int(winenertime_valeur):
            # The player was the fastest, we display it and record his score
            parameters = ConfigJson('./resources/config.json')
            ConfigJson.write_winner(parameters, time)
            text_win5 = "BEST TIME : " + self.cutHour(self.time_game)
            self.win5 = self.message.render(text_win5, True, (255, 255, 255))
        else:
            text_win5 = "Your time : " + self.cutHour(self.time_game)
            self.win5 = self.message.render(text_win5, True, (255, 255, 255))

        self.screen.blit(self.win5, (225, 350))

        # Initialization of variables
        self.time_game = 0
        self.level_number = 0
        pg.display.update()
        pg.time.delay(5000)

    def display_message_lost(self):
        """ End Game, the player has lost, the message is displayed and
            the time and level are initialized
        """

        self.rect = pg.draw.rect(self.screen, (155, 0, 0), [0, 300, 600, 50])
        self.screen.blit(self.lost, (110, 315))

        # Initialization of variables
        self.level_number = 0
        self.time_game = 0
        pg.display.update()
        pg.time.wait(2500)

    @staticmethod
    def cutHour(second):

        # Format the time
        if second > 59:
            minutes = round(second / 60)
            secondes = str(second % 60)
            if len(secondes) == 1:
                secondes = '0' + str(secondes)
            return str(minutes) + ':' + str(secondes)
        else:
            return str(second)

    def keyboard_events(self):
        """ Method for keyboard controllers during the game, implemented"""
        # into the game.start() method
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # We leave the game
                self.level_number = 0
                self.playing = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.macgyver.move_up(self.structure_map)
                elif event.key == pg.K_DOWN:
                    self.macgyver.move_down(self.structure_map)
                elif event.key == pg.K_RIGHT:
                    self.macgyver.move_right(self.structure_map)
                elif event.key == pg.K_LEFT:
                    self.macgyver.move_left(self.structure_map)
                elif event.type == pg.K_ESCAPE:
                    self.level_number = 0
                    self.playing = False

    def items_counter(self):
        """ Method to display the items counter, by using the Macgyver
            class to count the items number
        """
        #Text items
        self.counter_message = pg.font.SysFont(None, 25)
        text_items = "Items : " + str(self.macgyver.items_collected) + " / 3"
        self.counter = self.counter_message.render(text_items, True,((255, 255, 255)))
        self.screen.blit(self.counter, (45, 570))


        self.items_message = pg.font.SysFont(None, 25)
        text_items = str("["+self.macgyver.items_name_collected+"]")
        self.items = self.items_message.render(text_items, True,
                                                   ((255, 255, 255)))
        self.screen.blit(self.items, (150, 570))

        # Text Time
        self.time_message = pg.font.SysFont(None, 40)
        text_time = "Time : " + str(self.cutHour(self.time_game))
        self.timeDisplay = self.time_message.render(text_time, True,((255, 255, 255)))

        self.screen.blit(self.timeDisplay, (430, 7))
        pg.display.update()