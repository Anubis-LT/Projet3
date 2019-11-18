""""
Game: McGyver maze
Creator: Grégory Le Terte

Class: level.py
"""

import pygame as pgHome
import os
import sys

sys.path.append("./")
from resources.filepy.constants import *

class Level:
    def __init__(self,level):
        # Pygame initialization, screen and messages creation, """
        if level==0:
            # Init display game
            pgHome.init()
            pgHome.font.init()

            pgHome.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
            filesound = str(os.getcwd()+"/resources/sound/"+SOUND_MCGYVER)
            pgHome.mixer.music.set_volume(0.06)
            pgHome.mixer.music.load(filesound)
            pgHome.mixer.music.play()

            # Display
            sizeScreen      = int(SIZE_SPRITES*NB_SPRITES)
            self.screen     = pgHome.display.set_mode((sizeScreen,sizeScreen))
            self.title      = pgHome.display.set_caption(TITLE)
            self.icon       = pgHome.image.load(ICON).convert_alpha()
            pgHome.display.set_icon(self.icon)

            display_screen  = pgHome.image.load(LOGO).convert()
            self.screen.blit(display_screen, (0, 0))

            # Text choose level
            fontText        = pgHome.font.Font(None, 24)
            text_level      = fontText.render("::: 5 LEVELS :::", 1, (255, 255, 255))
            self.screen.blit(text_level, (250, 505))
            text_level = fontText.render("START THE GAME [ F1 ] ", 1, (255, 255, 255))
            self.screen.blit(text_level, (215, 533))

            # Display
            pgHome.display.flip()

            # Variable loop :  continue = True , Stop = False
            game_loop_menu = True

            self.pathfile       = ""
            self.numberLevel    = 0
            # Loop game Menu
            while game_loop_menu:

                # Limitation de vitesse de la boucle
                pgHome.time.Clock().tick(30)

                # Captured event
                for event in pgHome.event.get():

                    if event.type == pgHome.QUIT or (event.type == pgHome.KEYDOWN and event.key == pgHome.K_ESCAPE):

                        # exit the game
                        pgHome.quit()
                        return None
                    else:
                        if event.type == 3 and  pgHome.K_RETURN==13 and pgHome.KEYDOWN != 2:
                            nb = 1
                            self.pathfile = str(os.getcwd() + "/resources/maps/" + str(FILE_MAP) + str(nb) + ".txt")
                            self.numberLevel = nb
                            return None
                        elif event.type == 3 and pgHome.KEYDOWN == 2:

                            # launcher 1er level F1
                            nb = 1
                            if event.key == getattr(pgHome, f"K_F{nb}"):
                                self.pathfile       = str(os.getcwd()+"/resources/maps/"+str(FILE_MAP)+str(nb)+".txt")
                                self.numberLevel    = nb
                                return None

        else:
            # Next level
            level = level+1
            self.pathfile = str(os.getcwd() + "/resources/maps/" + str(FILE_MAP) + str(level) + ".txt")
            self.numberLevel = level
            return None
