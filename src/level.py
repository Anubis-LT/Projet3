#!/usr/bin/python3
# coding: Utf-8

"""
Game    : McGyver maze
File    : level.py
Creator : Grégory Le Terte
Info    : This program displays the window with the different levels
"""
import pygame as pgHome
import os
import sys

sys.path.append("./")
from src.constants import *
from src.configjson import ConfigJson


class Level:
    def __init__(self, level):
        """ If level == 0 launch the menu game else launch the level
            Args:
                level: Player level number
        """
        if level == 0:
            # Initialization of variables
            self.pathfile = ""
            self.numberLevel = 0

            # display menu
            self.display_menu()

            # music game
            self.manage_sound()

            # Variable loop menu:  continue = True , Stop = False
            self.game_loop_menu = True
            self.loop_game()
        else:
            # Next level
            level = level + 1
            self.path_file_number(level)
            return None

    def loop_game(self):
        # Loop game Menu
        while self.game_loop_menu:
            # Method should be called once per frame
            pgHome.time.Clock().tick(30)

            # Captured event
            for event in pgHome.event.get():
                if event.type == pgHome.QUIT or (
                        event.type == pgHome.KEYDOWN and event.key == pgHome.K_ESCAPE):
                    # Exit the game
                    pgHome.quit()
                    sys.exit(0)
                else:
                    # Launcher 1er level F1
                    if event.type == 3 and pgHome.KEYDOWN == 2:
                        level = 1
                        if event.key == getattr(pgHome, f"K_F{level}"):
                            self.path_file_number(level)
                            return None

    def path_file_number(self, number):
        """ return the path file txt ans the level number
            Args:
                number : level number
        """
        path_txt = "/resources/maps/" + str(FILE_MAP) + str(number) + ".txt"
        self.path_file = str(os.getcwd() + path_txt)
        self.number_level = number

    def manage_sound(self):
        # Manage sound
        pgHome.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        file_sound = str(os.getcwd() + "/resources/sound/" + SOUND_MCGYVER)
        pgHome.mixer.music.set_volume(0.90)
        pgHome.mixer.music.load(file_sound)
        pgHome.mixer.music.play()

    def display_menu(self):
        """ Display menu """
        # Pygame initialization
        pgHome.init()
        pgHome.font.init()

        # Display screen
        size_screen = int(SIZE_SPRITES * NB_SPRITES)
        self.screen = pgHome.display.set_mode((size_screen, size_screen))
        self.title = pgHome.display.set_caption(TITLE)
        self.icon = pgHome.image.load(ICON).convert_alpha()
        pgHome.display.set_icon(self.icon)

        display_screen = pgHome.image.load(LOGO).convert()
        self.screen.blit(display_screen, (0, 0))

        # Text choose level
        font_text = pgHome.font.Font(None, 35)
        text="START THE GAME [ F1 ] "
        text_level = font_text.render(text, 1,(255, 255, 255))
        self.screen.blit(text_level, (170, 490))

        font_text = pgHome.font.Font(None, 26)
        text = "5 levels to pass by picking up all the items in a " \
               "minimum of time"
        text_level = font_text.render(text, 1, (255, 255, 255))
        self.screen.blit(text_level, (37, 525))

        # Display Winner time
        font_text = pgHome.font.Font(None, 18)
        param = ConfigJson('./resources/config.json')
        const = ConfigJson.file_map(param, "constants")
        winner_time = const.get("winner_time")
        if len(WINNER_TIME) == 2:
            sformat = " sc."
        else:
            sformat = ""

        winner_date = constants.get("winner_date")
        text = "Best times : " + winner_date + " " + winner_time + sformat
        text_level = font_text.render(text, 1, (255, 255, 255))
        self.screen.blit(text_level, (225, 555))
        pgHome.display.flip()
